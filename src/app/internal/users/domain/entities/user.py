from ninja import Schema


class UserSchema(Schema):
    ...


class UserOut(UserSchema):
    ...


class UserIn(UserSchema):
    ...


class TelegramUserSchema(Schema):
    chat_id: int
    username: str | None
    first_name: str
    last_name: str | None


class TelegramUserIn(TelegramUserSchema):
    ...
