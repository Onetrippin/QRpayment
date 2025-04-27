from ninja import Router

from app.internal.users.presentation.rest.handlers import UserHandlers


def get_users_router(user_handlers: UserHandlers) -> Router:
    router = Router(tags=['users'])

    return router
