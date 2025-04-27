from app.internal.users.domain.services.user import UserService


class UserHandlers:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service
