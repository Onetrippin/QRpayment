from app.internal.transport_network.domain.interfaces.transport_network import ITransportNetworkRepository


class TransportNetworkService:
    def __init__(self, transport_network_repo: ITransportNetworkRepository) -> None:
        self.transport_network_repo = transport_network_repo
