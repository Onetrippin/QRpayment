from typing import List, Literal
from ninja import Schema


class NotificationIn(Schema):
    id: int
    enabled: bool
    stop_id: int
    days: List[Literal['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']]
    start: str
    end: str
    interval: int


class SetFavouriteRouteIn(Schema):
    route_id: int
    notifications: List[NotificationIn]


class SetFavouriteRouteOut(Schema):
    route_id: int
    transport_type: str
    route_number: str
    route_title: str
    price: int
    notice_number: int
