from abc import ABC, abstractmethod


class IFavouritesRepository(ABC):
    @abstractmethod
    def get_enabled_notifs(self, chat_id: int) -> list[dict]:
        ...

    @abstractmethod
    def disable_all_notifs(self, chat_id: int) -> None:
        ...

    @abstractmethod
    def get_or_create_favourite_route(self, user_id: int, route_id: int):
        ...

    @abstractmethod
    def create_default_notifications(self, user_id: int, favourite_id: int):
        ...

    @abstractmethod
    def update_notifications(self, user_id: int, favourite_id: int, notifications_data: list):
        ...

    @abstractmethod
    def get_route_info(self, route_id: int):
        ...

    @abstractmethod
    def delete_favourite_route(self, user_id: int, route_id: int):
        ...
