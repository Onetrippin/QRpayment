from app.internal.users.domain.entities.user import TelegramUserIn
from app.internal.users.domain.entities.user import UserCityIn
from app.internal.users.domain.interfaces.user import IUserRepository


class UserService:
    def __init__(self, user_repo: IUserRepository) -> None:
        self.user_repo = user_repo

    def add_user_if_not_exists(self, user_data: TelegramUserIn) -> None:
        return self.user_repo.add_user_if_not_exists(user_data)

    def get_city_by_chat_id(self, chat_id: int) -> str | None:
        return self.user_repo.get_city_by_chat_id(chat_id)

    def set_user_city(self, user_id: int, user_city_data: UserCityIn) -> bool:
        return self.user_repo.set_user_city(user_id, user_city_data)
