from app.internal.favourites.domain.interfaces.favourites import IFavouritesRepository


class FavouritesService:
    def __init__(self, favourites_repo: IFavouritesRepository) -> None:
        self.favourites_repo = favourites_repo

    def get_enabled_notifs(self, chat_id: int) -> list[dict]:
        return self.favourites_repo.get_enabled_notifs(chat_id)

    def disable_all_notifs(self, chat_id: int) -> None:
        self.favourites_repo.disable_all_notifs(chat_id)
