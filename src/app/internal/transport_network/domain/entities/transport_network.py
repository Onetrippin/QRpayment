from ninja import Schema


class TransportNetworkSchema(Schema):
    ...


class TransportNetworkOut(TransportNetworkSchema):
    routes: list


class TransportNetworkIn(TransportNetworkSchema):
    ...


class RouteOut(Schema):
    route_id: int
    route_number: str
    route_title: str
    city: str
    transports: list
    stops: list


class TransportInfoOut(Schema):
    route_title: str
    route_number: str
    state_number: str
    current_stop: str
    next_stop: str
    price: int
    qr_code_links: list[str]


class TransportInfoIn(Schema):
    state_number: str
    route_title: str
