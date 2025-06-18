from app.internal.favourites.domain.entities.favourites import SetFavouriteRouteIn, SetFavouriteRouteOut
from app.internal.favourites.domain.services.favourites import FavouritesService


class FavouritesHandlers:
    def __init__(self, favourites_service: FavouritesService) -> None:
        self.favourites_service = favourites_service

    def set_favourite_route(self, user_id: int, data: SetFavouriteRouteIn) -> SetFavouriteRouteOut:
        return self.favourites_service.set_favourite_route(user_id, data)

    def delete_favourite_route(self, user_id: int, route_id: int):
        return self.favourites_service.delete_favourite_route(user_id, route_id)