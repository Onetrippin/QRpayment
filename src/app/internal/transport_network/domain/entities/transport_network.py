from decimal import Decimal
from typing import List, Optional

from ninja import Schema


class RouteOut(Schema):
    route_id: int
    route_number: str
    route_title: str
    city: str
    transports: list
    stops: list


class PaymentTransportInfoOut(Schema):
    route_number: str
    route_title: str
    route_id: int
    transport_type: str
    state_number: str
    price: int
    is_favourite: bool
    current_stop: str
    next_stop: str
    user_uuid: str
    paytagid: list[dict]



class PaymentTransportInfoIn(Schema):
    transport_uuid: str


class UserCoordinatesIn(Schema):
    latitude: Decimal
    longitude: Decimal
    stop_type: Optional[str] = 'all'

    def to_decimal(self):
        return {
            "latitude": Decimal(self.latitude),
            "longitude": Decimal(self.longitude),
        }


class NearStopInfoOut(Schema):
    stop_id: int
    title: str
    next_stop_title: str
    routes: List[str]
    distance_km: float
    stop_type: str


class StopResponse(Schema):
    stops: List[NearStopInfoOut]



class NearestTransportIn(Schema):
    latitude: Decimal
    longitude: Decimal

    def to_decimal(self):
        return {
            "latitude": Decimal(self.latitude),
            "longitude": Decimal(self.longitude),
        }


class NearestTransportOut(Schema):
    transport_uuid: str
    transport_type: str
    route_number: str
    state_number: str   # из БД
    route_title: str
    route_id: int
    current_stop: str
    next_stop: str
    is_favourite: bool
    price: Decimal
    arrival_time: int  # заглушка

class NearestTransportsResponse(Schema):
    transports: List[NearestTransportOut]


class StopRouteOut(Schema):
    id: int
    route: str


class NextStopInfo(Schema):
    id: int
    name: str
    routes: List[StopRouteOut]


class StopTransportInfo(Schema):
    transport_uuid: str
    transport_type: str
    route_number: str
    state_number: str
    route_title: str
    price: int
    arrival_time: int


class StopInfoOut(Schema):
    stop_type: str
    stop_name: str
    next_stops: List[NextStopInfo]
    transports: List[StopTransportInfo]


class StopInfoIn(Schema):
    stop_id: int


class NearStopExtendedOut(Schema):
    stop_id: int
    stop_type: str
    stop_name: str
    stop_dist: float
    next_stop: List[NextStopInfo]
    transports: List[StopTransportInfo]


class NearStopsResponse(Schema):
    stops: List[NearStopInfoOut]


class TransportInfoIn:
    pass