from ninja import Router

from app.internal.favourites.presentation.rest.handlers import FavouritesHandlers


def get_favourites_router(favourites_handlers: FavouritesHandlers) -> Router:
    router = Router(tags=['favourites'])

    return router
