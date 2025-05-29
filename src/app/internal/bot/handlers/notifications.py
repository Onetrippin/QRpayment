from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import CallbackContext

from app.internal.bot.keyboards import get_dis_notif_keyboard
from app.internal.favourites.data.repositories.favourites import FavouritesRepository
from app.internal.favourites.domain.services.favourites import FavouritesService

favourites_repo = FavouritesRepository()
favourites_service = FavouritesService(favourites_repo=favourites_repo)


async def notifications_list(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.from_user.id
    enabled_notifs = await sync_to_async(favourites_service.get_enabled_notifs)(chat_id=chat_id)
    if enabled_notifs:
        emoji = {
            'bus': '🚌',
            'trol': '🚎',
            'tram': '🚋',
        }
        status = 'включены ✅'

        grouped = {}
        for notif in enabled_notifs:
            city = notif.get('favourite_route__route__city__name')
            if city not in grouped:
                grouped[city] = []
            grouped[city].append(notif)

        lines = []
        for city, notifs in grouped.items():
            lines.append(f'🏙️ {city}')
            for notif in notifs:
                line = (
                    f'{emoji.get(notif.get("favourite_route__route__transport_type"))} '
                    f'№{notif.get("favourite_route__route__number")} '
                    f'\"{notif.get("favourite_route__route__title")}\"\n'
                    f'🚏 {notif.get("stop__title")}\n'
                    f'📅 {", ".join(notif.get("days"))}\n'
                    f'🕔 {notif.get("time_from").strftime("%H:%M")}-{notif.get("time_to").strftime("%H:%M")}'
                )
                lines.append(line)

        addition = '\n\n\n' + '\n\n'.join(lines)
        reply_markup = await get_dis_notif_keyboard()
    else:
        status = 'отключены ❌'
        addition = '\n\nТы можешь включить и настроить их через мини-приложение'
        reply_markup = None
    text = f'📲 Уведомления сейчас {status}{addition}'[:4096]
    await update.message.reply_text(text, reply_markup=reply_markup)


async def disable_notifs(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    chat_id = query.from_user.id
    await sync_to_async(favourites_service.disable_all_notifs)(chat_id=chat_id)
    await query.answer(text='Готово')
    await query.edit_message_text(
        '🔕 Уведомления временно отключены. Ты можешь включить их обратно через мини-приложение'
    )
