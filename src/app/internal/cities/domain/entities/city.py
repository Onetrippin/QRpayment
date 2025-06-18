from ninja import Schema


class CitySchema(Schema):
    id: int
    name: str
    is_active: bool
