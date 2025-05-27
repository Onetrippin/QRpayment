from telegram import Update
from telegram.ext import CallbackContext

from app.internal.bot.decorators import add_user_if_not_exists
from app.internal.bot.keyboards import get_main_menu_keyboard
from app.internal.bot.texts import HELP_MESSAGE, START_MESSAGE


@add_user_if_not_exists
async def start_handler(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(START_MESSAGE, reply_markup=await get_main_menu_keyboard())


@add_user_if_not_exists
async def help_handler(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(HELP_MESSAGE, reply_markup=await get_main_menu_keyboard())


async def other(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('<b>Пользуйся кнопками!</b>', reply_markup=await get_main_menu_keyboard())
