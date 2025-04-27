from datetime import datetime
from decimal import Decimal

from ninja import Schema


class PastRideOut(Schema):
    route_number: str
    route_name: str
    transport_type: str
    transport_state_number: str
    price: Decimal
    date: datetime


class PastRideIn(Schema):
    transport_id: int
    price: Decimal


class AddedPastRideOut(Schema):
    user_id: int
    transport_id: int
    price: Decimal
