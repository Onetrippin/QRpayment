from http import HTTPStatus

from ninja import Body

from app.internal.common.response_entities import ErrorResponse
from app.internal.transport_network.domain.entities.transport_network import TransportInfoIn
from app.internal.transport_network.domain.services.transport_network import TransportNetworkService


class TransportNetworkHandlers:
    def __init__(self, transport_network_service: TransportNetworkService) -> None:
        self.transport_network_service = transport_network_service

    def get_transport_info(self, request, transport_info_data: TransportInfoIn = Body(...)):
        transport_info = self.transport_network_service.get_transport_info(transport_info_data)

        if not transport_info:
            return HTTPStatus.NOT_FOUND, ErrorResponse(error='Транспорт не найден')

        return HTTPStatus.OK, transport_info
