from http import HTTPStatus

from ninja import Body, Router

from app.internal.common.response_entities import ErrorResponse
from app.internal.users.domain.entities.user import UserCityIn
from app.internal.users.presentation.rest.handlers import UserHandlers


def get_users_router(user_handlers: UserHandlers) -> Router:
    router = Router(tags=['users'])

    @router.get(
        'user/set_city',
        response={HTTPStatus.OK: bool, HTTPStatus.NOT_FOUND: ErrorResponse},
        summary='Установка города пользователю'
    )
    def set_user_city(self, request, user_city_data: UserCityIn = Body(...)):
        return user_handlers.set_user_city(request, user_city_data)

    return router
