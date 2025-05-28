from django.conf import settings
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo


async def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton('💳 Оплатить проезд', web_app=WebAppInfo(url=settings.MINIAPP_URL))],
            [KeyboardButton('🚀 Быстрая оплата'), KeyboardButton('🔔 Уведомления')],
            [KeyboardButton('❓ Помощь'), KeyboardButton('📞 Поддержка')],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


async def get_dis_notif_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton('🔕 Временно отключить', callback_data='disable_notifs')]]
    )


async def get_support_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton('❌ Отмена')]], resize_keyboard=True, one_time_keyboard=True)


async def get_fast_pay_keyboard(city: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton('🔍 Найти транспорт', switch_inline_query_current_chat=f'{city} ')]]
    )


async def get_qr_links_keyboard(pay_tags: list[str]) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='💳 Оплатить проезд', url=f'https://qr.bilet.nspk.ru/payment?paytagid={pay_tags[0]}')]
    ]
    additional = [
        InlineKeyboardButton(text=f'Доп. ссылка {i + 1}', url=f'https://qr.bilet.nspk.ru/payment?paytagid={tag}')
        for i, tag in enumerate(pay_tags[1:])
    ]
    for i in range(0, len(additional), 2):
        buttons.append(additional[i : i + 2])

    return InlineKeyboardMarkup(buttons)
