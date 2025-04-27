from ninja import NinjaAPI

from app.internal.users.data.repositories.user import UserRepository
from app.internal.users.domain.services.user import UserService
from app.internal.users.presentation.rest.handlers import UserHandlers
from app.internal.users.presentation.rest.routers import get_users_router


def add_users_router(api: NinjaAPI, path: str) -> None:
    user_repo = UserRepository()
    user_service = UserService(user_repo=user_repo)
    user_handlers = UserHandlers(user_service=user_service)

    users_router = get_users_router(user_handlers)
    api.add_router(path, users_router)
