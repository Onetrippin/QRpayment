from abc import ABC, abstractmethod

from app.internal.users.domain.entities.user import TelegramUserIn


class IUserRepository(ABC):
    @abstractmethod
    def add_user_if_not_exists(self, user_data: TelegramUserIn) -> None:
        ...

    @abstractmethod
    def get_city_by_chat_id(self, chat_id: int) -> str | None:
        ...
