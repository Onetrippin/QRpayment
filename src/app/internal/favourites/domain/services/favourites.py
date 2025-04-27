from app.internal.favourites.domain.interfaces.favourites import IFavouritesRepository


class FavouritesService:
    def __init__(self, favourites_repo: IFavouritesRepository) -> None:
        self.favourites_repo = favourites_repo
        