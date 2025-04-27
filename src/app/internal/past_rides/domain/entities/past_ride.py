from datetime import datetime

from ninja import Schema


class PastRideOut(Schema):
    route_number: str
    route_title: str
    transport_type: str
    transport_state_number: str
    price: int
    date: datetime


class PastRideIn(Schema):
    transport_id: int
    price: int


class AddedPastRideOut(Schema):
    user_id: int
    transport_id: int
    price: int
