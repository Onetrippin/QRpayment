from abc import ABC, abstractmethod


class IFavouritesRepository(ABC):
    @abstractmethod
    def get_enabled_notifs(self, chat_id: int) -> list[dict]:
        ...

    @abstractmethod
    def disable_all_notifs(self, chat_id: int) -> None:
        ...
