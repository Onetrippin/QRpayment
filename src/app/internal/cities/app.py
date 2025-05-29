from ninja import NinjaAPI

from app.internal.cities.data.repositories.city import CityRepository
from app.internal.cities.domain.services.city import CityService
from app.internal.cities.presentation.rest.handlers import CityHandlers
from app.internal.cities.presentation.rest.routers import get_cities_router


def add_cities_router(api: NinjaAPI, path: str) -> None:
    city_repo = CityRepository()
    city_service = CityService(city_repo=city_repo)
    city_handlers = CityHandlers(city_service=city_service)

    cities_router = get_cities_router(city_handlers)
    api.add_router(path, cities_router)
