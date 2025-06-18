from ninja import Schema


class UserCityIn(Schema):
    city_id: int


class TelegramUserSchema(Schema):
    chat_id: int
    username: str | None
    first_name: str
    last_name: str | None


class TelegramUserIn(TelegramUserSchema):
    ...
