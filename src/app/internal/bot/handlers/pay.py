from uuid import uuid4

from asgiref.sync import sync_to_async
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import CallbackContext

from app.internal.bot.decorators import add_user_if_not_exists
from app.internal.bot.inline_mode_answers import get_answer_query_is_empty, get_result_no_search_str, \
    get_result_not_valid_city, get_result_no_results
from app.internal.bot.keyboards import get_fast_pay_keyboard, get_qr_links_keyboard
from app.internal.cities.data.repositories.city import CityRepository
from app.internal.cities.domain.services.city import CityService
from app.internal.transport_network.data.repositories.transport_network import TransportNetworkRepository
from app.internal.transport_network.domain.services.transport_network import TransportNetworkService
from app.internal.users.data.repositories.user import UserRepository
from app.internal.users.domain.services.user import UserService

user_repo = UserRepository()
user_service = UserService(user_repo=user_repo)
transport_network_repo = TransportNetworkRepository()
transport_network_service = TransportNetworkService(transport_network_repo=transport_network_repo)
city_repo = CityRepository()
city_service = CityService(city_repo=city_repo)


async def fast_pay(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    city = await sync_to_async(user_service.get_city_by_chat_id)(chat_id=chat_id)
    if not city:
        city = 'Екатеринбург'
    await update.message.reply_text(
        'Нажми на кнопку, чтобы найти нужный тебе транспорт', reply_markup=await get_fast_pay_keyboard(city=city)
    )


@add_user_if_not_exists
async def inline_mode_pay(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    if not query:
        await update.inline_query.answer(await get_answer_query_is_empty(), is_personal=False, cache_time=86400)
        return
    parts = query.strip().split(maxsplit=1)
    if len(parts) < 2:
        city = parts[0].strip()
        search_query = ''
    else:
        city, search_query = parts
    offset = int(update.inline_query.offset) if update.inline_query.offset else 0
    limit = 50
    results = []
    if not search_query and offset == 0:
        if await sync_to_async(city_service.is_city_valid)(city=city):
            results.append(await get_result_no_search_str(query))
        else:
            results.append(await get_result_not_valid_city(city))
        limit -= 1
    transports = await sync_to_async(transport_network_service.get_transport)(
        city=city,
        query=search_query,
        offset=offset,
        limit=limit+1,
    )
    has_next_page = len(transports) > limit
    transport_logo = {
        'bus': 'https://img.icons8.com/?size=100&id=COfeCP0ZqQKk&format=png&color=000000',
        'trol': 'https://img.icons8.com/?size=100&id=fIIIRQVdZWjH&format=png&color=000000',
        'tram': 'https://img.icons8.com/?size=100&id=QhDRQuByCL0n&format=png&color=000000',
    }
    emoji = {'bus': '🚌', 'trol': '🚎', 'tram': '🚋'}
    for index, transport in enumerate(transports[:limit]):
        pay_tag_ids = transport.get('pay_tag_ids') or []
        if not pay_tag_ids:
            continue
        pay_url = f'https://qr.bilet.nspk.ru/payment?paytagid={pay_tag_ids[0]}'
        keyboard = await get_qr_links_keyboard(pay_tag_ids)
        title = f'№{transport.get("route__number")} \"{transport.get("route__title")}\"'
        description = f'Госномер: {transport.get("state_number")}'
        text = (
            f'{emoji.get(transport.get("type"))} №{transport.get("route__number")} '
            f'\"{transport.get("route__title")}\"\n'
            f'Госномер: {transport.get("state_number")}\n\n'
            f'Для оплаты проезда нажми на кнопку <b><i>💳 Оплатить проезд</i></b> '
            f'или воспользуйся <i>дополнительными</i> ссылками, если основная не работает'
        )
        results.append(
            InlineQueryResultArticle(
                id=f'{transport["route__number"]}_{transport["state_number"]}',
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(text, disable_web_page_preview=True),
                reply_markup=keyboard,
                url=pay_url,
                thumbnail_url=transport_logo.get(transport.get('type')),
            )
        )
    if not results:
        results.append(await get_result_no_results(query))
    next_offset = str(offset + limit) if has_next_page else ''
    await update.inline_query.answer(results, cache_time=600, is_personal=False, next_offset=next_offset)
