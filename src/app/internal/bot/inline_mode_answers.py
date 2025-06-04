from telegram import InlineQueryResultArticle, InputTextMessageContent

from app.internal.bot.keyboards import get_inline_mode_hint_keyboard


async def get_answer_query_is_empty() -> list:
    return [
        InlineQueryResultArticle(
            id='empty',
            title='Подсказка',
            input_message_content=InputTextMessageContent(
                message_text=(
                    'Введи <b>город</b>, а затем <b>поисковой запрос</b>, разделяя пробелами, '
                    'например, <code>@pay4ridebot Екатеринбург АБВ</code>'
                ),
                disable_web_page_preview=True,
            ),
            description=(
                'Введи город, а затем поисковый запрос, разделяя пробелами, например, "@pay4ridebot Екатеринбург АБВ"'
            ),
            thumbnail_url='https://img.icons8.com/?size=100&id=63684&format=png&color=000000',
            reply_markup=await get_inline_mode_hint_keyboard(),
        )
    ]


async def get_result_no_search_str(query: str) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        id='no_search_str',
        title='Подсказка',
        input_message_content=InputTextMessageContent(
            message_text='Введи <b>номер маршрута</b> или <b>госномер</b>, чтобы найти нужный транспорт',
            disable_web_page_preview=True,
        ),
        description='Введи номер маршрута или госномер, чтобы найти нужный транспорт',
        thumbnail_url='https://img.icons8.com/?size=100&id=63684&format=png&color=000000',
        reply_markup=await get_inline_mode_hint_keyboard(query.title()),
    )


async def get_result_not_valid_city(city: str) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        id='not_valid_city',
        title='Город не найден',
        input_message_content=InputTextMessageContent(
            message_text=f'В нашем приложении пока что нет города <b>{city.title()}</b>, но мы уже работаем над этим',
            disable_web_page_preview=True,
        ),
        description=f'В нашем приложении пока что нет города "{city.title()}", но мы уже работаем над этим',
        thumbnail_url='https://img.icons8.com/?size=100&id=20732&format=png&color=000000',
        reply_markup=await get_inline_mode_hint_keyboard(),
    )


# async def get_result_no_results(query: str) -> InlineQueryResultArticle:
#     return InlineQueryResultArticle(
#         id='no_results',
#         title='Ничего не найдено',
#         input_message_content=InputTextMessageContent(
#             message_text='<b><i>Ничего не найдено...</i></b>\n\n'
#             'Проверь, правильно ли ты ввёл <b>город</b> и <b>номер маршрута/госномер</b>',
#             disable_web_page_preview=True,
#         ),
#         description='Возможно, ты ошибся при вводе',
#         thumbnail_url='https://img.icons8.com/?size=100&id=20732&format=png&color=000000',
#         reply_markup=await get_inline_mode_hint_keyboard(query.split()[0].title()),
#     )
