from django.conf import settings
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo


async def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton('Оплатить проезд', web_app=WebAppInfo(url=settings.MINIAPP_URL))],
            [KeyboardButton('Быстрая оплата'), KeyboardButton('Уведомления')],
            [KeyboardButton('Помощь'), KeyboardButton('Поддержка')],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


async def get_dis_notif_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton('🔕 Временно отключить', callback_data='disable_notifs')]]
    )


async def get_support_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton('Отмена')]], resize_keyboard=True, one_time_keyboard=True)


async def get_fast_pay_keyboard(city: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton('🔍 Найти транспорт', switch_inline_query_current_chat=f'{city} ')]]
    )
