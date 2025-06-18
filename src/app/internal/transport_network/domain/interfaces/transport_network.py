from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Optional

from django.db.models import QuerySet

from app.internal.transport_network.data.models.stop import Stop
from app.internal.transport_network.domain.entities.transport_network import (
    NearestTransportOut,
    PaymentTransportInfoIn,
    PaymentTransportInfoOut,
    StopInfoIn,
    StopInfoOut,
)


class ITransportNetworkRepository(ABC):
    @abstractmethod
    def get_transport(self, city: str, query: str, offset: int, limit: int = 51) -> list[dict]:
        ...

    @abstractmethod
    def get_transport_info(self, transport_info_data: PaymentTransportInfoIn, user_id: int, user_uuid: str) -> Optional[
        PaymentTransportInfoOut]:
        ...

    @abstractmethod
    def get_stops_within_radius(self, latitude: Decimal, longitude: Decimal,
                                radius_km: Decimal = Decimal("1.0")) -> QuerySet[Stop]:
        ...

    @abstractmethod
    def get_nearest_transports(self, user_id: int, lat: Decimal, lon: Decimal) -> List[NearestTransportOut]:
        ...

    @abstractmethod
    def get_stop_info(self, stop_info_data: StopInfoIn) -> Optional[StopInfoOut]:
        ...
