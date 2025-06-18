from http import HTTPStatus

from app.internal.cities.domain.services.city import CityService
from app.internal.common.response_entities import ErrorResponse


class CityHandlers:
    def __init__(self, city_service: CityService) -> None:
        self.city_service = city_service

    def get_cities_list(self, request):
        cities_list = self.city_service.get_cities_list(request)

        if not cities_list:
            return HTTPStatus.NOT_FOUND, ErrorResponse(error='Города не найдены')

        return HTTPStatus.OK, cities_list
