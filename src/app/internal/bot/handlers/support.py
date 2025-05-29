from django.conf import settings
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from app.internal.bot.keyboards import get_main_menu_keyboard, get_support_keyboard
from app.internal.bot.texts import SUPPORT_MESSAGE


async def support_handler(update: Update, context: CallbackContext) -> str:
    await update.message.reply_text(SUPPORT_MESSAGE, reply_markup=await get_support_keyboard())
    return 'wait_message'


async def wait_message(update: Update, context: CallbackContext) -> int:
    message_id = update.message.message_id
    chat_id = update.message.chat_id
    channel_id = settings.TELEGRAM_CHANNEL_ID
    user = update.message.from_user

    await context.bot.send_message(chat_id=channel_id, text=f'От пользователя @{user.username} (id:{user.id}):')
    await context.bot.forward_message(chat_id=channel_id, from_chat_id=chat_id, message_id=message_id)
    await update.message.reply_text('✅ Сообщение отправлено в поддержку', reply_markup=await get_main_menu_keyboard())
    return ConversationHandler.END


async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        '<b>Отправка сообщения в поддержку отменена</b>', reply_markup=await get_main_menu_keyboard()
    )
    return ConversationHandler.END
