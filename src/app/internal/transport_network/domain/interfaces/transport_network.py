from abc import ABC, abstractmethod
from typing import Optional

from app.internal.transport_network.domain.entities.transport_network import TransportInfoIn, TransportInfoOut


class ITransportNetworkRepository(ABC):
    @abstractmethod
    def get_transport(self, city: str, query: str, offset: int, limit: int = 51) -> list[dict]:
        ...

    @abstractmethod
    def get_transport_info(self, transport_info_data: TransportInfoIn) -> Optional[TransportInfoOut]:
        ...
