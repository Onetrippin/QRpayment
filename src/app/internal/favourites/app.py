from ninja import NinjaAPI

from app.internal.favourites.data.repositories.favourites import FavouritesRepository
from app.internal.favourites.domain.services.favourites import FavouritesService
from app.internal.favourites.presentation.rest.handlers import FavouritesHandlers
from app.internal.favourites.presentation.rest.routers import get_favourites_router


def add_favourites_router(api: NinjaAPI, path: str) -> None:
    favourites_repo = FavouritesRepository()
    favourites_service = FavouritesService(favourites_repo=favourites_repo)
    favourites_handlers = FavouritesHandlers(favourites_service=favourites_service)

    favourites_router = get_favourites_router(favourites_handlers)
    api.add_router(path, favourites_router)
