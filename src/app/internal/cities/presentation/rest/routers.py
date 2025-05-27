from http import HTTPStatus

from ninja import Router

from app.internal.cities.domain.entities.city import CitySchema
from app.internal.cities.presentation.rest.handlers import CityHandlers
from app.internal.common.response_entities import ErrorResponse


def get_cities_router(city_handlers: CityHandlers) -> Router:
    router = Router(tags=['cities'])

    @router.get(
        '/cities',
        response={HTTPStatus.OK: CitySchema, HTTPStatus.NOT_FOUND: ErrorResponse},
        summary='Получение списка всех городов',
    )
    def get_cities_list(request):
        return city_handlers.get_cities_list(request)

    return router
