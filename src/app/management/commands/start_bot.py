from django.conf import settings
from django.core.management.base import BaseCommand

from app.internal.bot.bot import build_bot


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        mode = ('webhook', 'polling')[settings.DEBUG]
        bot = build_bot()
        try:
            if mode == 'polling':
                bot.run_polling()
            else:
                bot.run_webhook(
                    listen='0.0.0.0',
                    port=settings.WEBHOOK_PORT,
                    url_path='',
                    secret_token=settings.TELEGRAM_WEBHOOK_TOKEN,
                    webhook_url=f'https://{settings.TELEGRAM_WEBHOOK_URL}/',
                    drop_pending_updates=True,
                    close_loop=False,
                )
        except Exception as e:
            print(f'Ошибка при работе бота: {e}')
        finally:
            bot.stop()
