from abc import ABC, abstractmethod


class ITransportNetworkRepository(ABC):
    @abstractmethod
    def get_transport(self, city: str, query: str, offset: int, limit: int = 51) -> list[dict]:
        ...
