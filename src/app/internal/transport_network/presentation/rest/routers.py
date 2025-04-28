from http import HTTPStatus

from ninja import Body, Router

from app.internal.common.response_entities import ErrorResponse
from app.internal.transport_network.domain.entities.transport_network import TransportInfoIn, TransportInfoOut
from app.internal.transport_network.presentation.rest.handlers import TransportNetworkHandlers


def get_transport_network_router(transport_network_handlers: TransportNetworkHandlers) -> Router:
    router = Router(tags=['transport_network'])

    @router.post(
        '/transport_info',
        response={HTTPStatus.OK: TransportInfoOut, HTTPStatus.NOT_FOUND: ErrorResponse},
        summary='Получение информации о транспорте',
    )
    def get_transport_info(request, transport_info_data: TransportInfoIn = Body(...)):
        return transport_network_handlers.get_transport_info(request, transport_info_data)

    return router
