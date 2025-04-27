from app.internal.favourites.domain.services.favourites import FavouritesService


class FavouritesHandlers:
    def __init__(self, favourites_service: FavouritesService) -> None:
        self.favourites_service = favourites_service
