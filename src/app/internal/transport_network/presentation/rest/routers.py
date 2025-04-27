from ninja import Router

from app.internal.transport_network.presentation.rest.handlers import TransportNetworkHandlers


def get_transport_network_router(transport_network_handlers: TransportNetworkHandlers) -> Router:
    router = Router(tags=['transport_network'])

    return router
