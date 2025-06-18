from http import HTTPStatus

from ninja import Body

from app.internal.common.response_entities import ErrorResponse
from app.internal.users.domain.entities.user import UserCityIn
from app.internal.users.domain.services.user import UserService


class UserHandlers:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def set_user_city(self, request, user_city_data: UserCityIn = Body(...)):
        user_id = request.user_id
        success = self.user_service.set_user_city(user_id, user_city_data)

        if not success:
            return HTTPStatus.NOT_FOUND, ErrorResponse(error="Такого города не существует")

        return HTTPStatus.OK, True
