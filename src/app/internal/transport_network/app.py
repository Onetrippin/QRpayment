from ninja import NinjaAPI

from app.internal.transport_network.data.repositories.transport_network import TransportNetworkRepository
from app.internal.transport_network.domain.services.transport_network import TransportNetworkService
from app.internal.transport_network.presentation.rest.handlers import TransportNetworkHandlers
from app.internal.transport_network.presentation.rest.routers import get_transport_network_router


def add_transport_network_router(api: NinjaAPI, path: str) -> None:
    transport_network_repo = TransportNetworkRepository()
    transport_network_service = TransportNetworkService(transport_network_repo=transport_network_repo)
    transport_network_handlers = TransportNetworkHandlers(transport_network_service=transport_network_service)

    transport_network_router = get_transport_network_router(transport_network_handlers)
    api.add_router(path, transport_network_router)
