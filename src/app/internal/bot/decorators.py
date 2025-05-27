from functools import wraps

from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import CallbackContext

from app.internal.users.data.repositories.user import UserRepository
from app.internal.users.domain.entities.user import TelegramUserIn
from app.internal.users.domain.services.user import UserService

user_repo = UserRepository()
user_service = UserService(user_repo=user_repo)


def add_user_if_not_exists(func):
    @wraps(func)
    async def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
        user = update.effective_user
        await sync_to_async(user_service.add_user_if_not_exists)(
            TelegramUserIn(
                chat_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
            )
        )
        return await func(update, context, *args, **kwargs)

    return wrapper
