from http import HTTPStatus

from ninja import Body

from app.internal.common.response_entities import ErrorResponse
from app.internal.transport_network.domain.entities.transport_network import (
    NearestTransportsResponse,
    PaymentTransportInfoIn,
    StopInfoIn,
    StopResponse,
    UserCoordinatesIn,
    NearStopsResponse,
    NearestTransportIn,
)
from app.internal.transport_network.domain.services.transport_network import TransportNetworkService


class TransportNetworkHandlers:
    def __init__(self, transport_network_service: TransportNetworkService) -> None:
        self.transport_network_service = transport_network_service

    def get_transport_info(self, request, transport_info_data: PaymentTransportInfoIn = Body(...)):
        transport_info = self.transport_network_service.get_transport_info(
            transport_info_data,
            user_id=request.user_id,
            user_uuid=str(request.user_uuid)
        )

        if not transport_info:
            return HTTPStatus.NOT_FOUND, ErrorResponse(error='Транспорт не найден')

        return HTTPStatus.OK, transport_info

    def get_stops_within_radius(self, request, user_coordinates_data: UserCoordinatesIn):
        coords = user_coordinates_data.to_decimal()

        stops = self.transport_network_service.get_stops_within_radius(
            coords["latitude"],
            coords["longitude"],
            stop_type_filter=user_coordinates_data.stop_type,
        )

        if not stops:
            return HTTPStatus.NOT_FOUND, ErrorResponse(error="Остановки не найдены")

        return HTTPStatus.OK, NearStopsResponse(stops=stops)

    def get_nearest_transports(self, request, query: NearestTransportIn):
        user_id = request.user.id
        coords = query.to_decimal()
        transports = self.transport_network_service.get_nearest_transports(
            user_id=user_id,
            lat=coords["latitude"],
            lon=coords["longitude"],
        )

        if not transports:
            return HTTPStatus.NOT_FOUND, ErrorResponse(error="Транспортные средства не найдены")

        return HTTPStatus.OK, NearestTransportsResponse(transports=transports)

    def get_stop_info(self, request, stop_info_data: StopInfoIn = Body(...)):
        stop_info = self.transport_network_service.get_stop_info(stop_info_data)

        if not stop_info:
            return HTTPStatus.NOT_FOUND, ErrorResponse(error="Остановка не найдена")

        return HTTPStatus.OK, stop_info
