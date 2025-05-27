from django.core.management.base import BaseCommand

from app.internal.bot.bot import build_bot


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        bot = build_bot()
        try:
            bot.run_polling()
        except Exception as e:
            print(f'Ошибка при работе бота: {e}')
        finally:
            bot.stop()
