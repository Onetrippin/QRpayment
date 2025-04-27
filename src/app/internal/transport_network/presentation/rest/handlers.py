from app.internal.transport_network.domain.services.transport_network import TransportNetworkService


class TransportNetworkHandlers:
    def __init__(self, transport_network_service: TransportNetworkService) -> None:
        self.transport_network_service = transport_network_service
