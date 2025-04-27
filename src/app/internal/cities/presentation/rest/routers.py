from ninja import Router

from app.internal.cities.presentation.rest.handlers import CityHandlers


def get_cities_router(city_handlers: CityHandlers) -> Router:
    router = Router(tags=['cities'])

    return router
