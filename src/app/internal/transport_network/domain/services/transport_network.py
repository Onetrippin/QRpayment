from app.internal.transport_network.domain.interfaces.transport_network import ITransportNetworkRepository


class TransportNetworkService:
    def __init__(self, transport_network_repo: ITransportNetworkRepository) -> None:
        self.transport_network_repo = transport_network_repo

    def get_transport(self, city: str, query: str, offset: int, limit: int = 51) -> list[dict]:
        return self.transport_network_repo.get_transport(city, query, offset, limit)
