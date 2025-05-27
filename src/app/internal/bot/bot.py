from django.conf import settings
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    Defaults,
    InlineQueryHandler,
    MessageHandler,
    filters,
)

from app.internal.bot.handlers.default import help_handler, other, start_handler
from app.internal.bot.handlers.notifications import disable_notifs, notifications_list
from app.internal.bot.handlers.pay import fast_pay, inline_mode_pay
from app.internal.bot.handlers.support import cancel, support_handler, wait_message


def build_bot() -> Application:
    bot = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).defaults(Defaults(parse_mode=ParseMode.HTML)).build()
    bot.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(filters.Text(['Поддержка']), support_handler)],
            states={
                'wait_message': [
                    MessageHandler(filters.ALL & ~filters.Text(['Отмена']), wait_message),
                ]
            },
            fallbacks=[MessageHandler(filters.TEXT, cancel)],
        )
    )
    bot.add_handler(CommandHandler('start', start_handler))
    bot.add_handler(
        MessageHandler(filters.TEXT & (filters.Regex(r'(?i)^/help(\s|$)') | filters.Text(['Помощь'])), help_handler)
    )
    bot.add_handler(MessageHandler(filters.Text(['Уведомления']), notifications_list))
    bot.add_handler(MessageHandler(filters.Text(['Быстрая оплата']), fast_pay))
    bot.add_handler(CallbackQueryHandler(disable_notifs))
    bot.add_handler(InlineQueryHandler(inline_mode_pay))
    bot.add_handler(MessageHandler(filters.ALL, other))
    return bot
