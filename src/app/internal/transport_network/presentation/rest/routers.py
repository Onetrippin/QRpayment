from http import HTTPStatus

from ninja import Body, Router

from app.internal.common.response_entities import ErrorResponse
from app.internal.transport_network.domain.entities.transport_network import (
    NearestTransportsResponse,
    PaymentTransportInfoIn,
    PaymentTransportInfoOut,
    StopInfoIn,
    StopInfoOut,
    UserCoordinatesIn,
    NearStopsResponse,
    NearestTransportIn,
)
from app.internal.transport_network.presentation.rest.handlers import TransportNetworkHandlers


def get_transport_network_router(transport_network_handlers: TransportNetworkHandlers) -> Router:
    router = Router(tags=['transport_network'])

    @router.post(
        '/transport_info',
        response={HTTPStatus.OK: PaymentTransportInfoOut, HTTPStatus.NOT_FOUND: ErrorResponse},
        summary='Получение информации о транспорте на странице оплаты',
    )
    def get_transport_info(request, transport_info_data: PaymentTransportInfoIn = Body(...)):
        return transport_network_handlers.get_transport_info(request, transport_info_data)

    @router.post(
        "/stops_within_radius",
        response={HTTPStatus.OK: NearStopsResponse, HTTPStatus.NOT_FOUND: ErrorResponse},
        summary="Получение остановок в радиусе 1 км",
    )
    def get_stops_within_radius(request, user_coordinates_data: UserCoordinatesIn):
        return transport_network_handlers.get_stops_within_radius(request, user_coordinates_data)

    @router.post(
        "/nearest_transports",
        response={HTTPStatus.OK: NearestTransportsResponse, HTTPStatus.NOT_FOUND: ErrorResponse},
        summary="Получение ближайших транспортных средств по координатам",
    )
    def get_nearest_transports(request, query: NearestTransportIn):
        return transport_network_handlers.get_nearest_transports(request, query)

    @router.post(
        "/stop_info",
        response={HTTPStatus.OK: StopInfoOut, HTTPStatus.NOT_FOUND: ErrorResponse},
        summary="Получение информации об остановке по ID"
    )
    def get_stop_info(request, stop_info_data: StopInfoIn = Body(...)):
        return transport_network_handlers.get_stop_info(request, stop_info_data)

    return router
