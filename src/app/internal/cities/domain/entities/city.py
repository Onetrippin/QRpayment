from ninja import Schema


class CitySchema(Schema):
    city_id: int
    city_name: str
    is_active: bool
