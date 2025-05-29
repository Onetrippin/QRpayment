from http import HTTPStatus

from ninja import Body, Router

from app.internal.common.response_entities import ErrorResponse
from app.internal.users.presentation.rest.handlers import UserHandlers


def get_users_router(user_handlers: UserHandlers) -> Router:
    router = Router(tags=['users'])
    return router
