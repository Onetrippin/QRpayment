from decimal import Decimal
from typing import List, Optional

from app.internal.transport_network.domain.entities.transport_network import (
    NearestTransportOut,
    NearStopInfoOut,
    PaymentTransportInfoIn,
    PaymentTransportInfoOut,
    StopInfoIn,
    StopInfoOut,
)
from app.internal.transport_network.domain.interfaces.transport_network import ITransportNetworkRepository


class TransportNetworkService:
    def __init__(self, transport_network_repo: ITransportNetworkRepository) -> None:
        self.transport_network_repo = transport_network_repo

    def get_transport(self, city: str, query: str, offset: int, limit: int = 51) -> list[dict]:
        return self.transport_network_repo.get_transport(city, query, offset, limit)

    def get_transport_info(self, transport_info_data: PaymentTransportInfoIn, user_id: int, user_uuid: str) -> Optional[
        PaymentTransportInfoOut]:
        return self.transport_network_repo.get_transport_info(transport_info_data, user_id, user_uuid)

    def get_stops_within_radius(
            self,
            latitude: Decimal,
            longitude: Decimal,
            radius_km: Decimal = Decimal("1.0"),
            stop_type_filter: str = "all"
    ) -> List[NearStopInfoOut]:
        raw_stops = self.transport_network_repo.get_stops_within_radius(latitude, longitude, radius_km)
        result = []
        for stop in raw_stops:
            if stop_type_filter != "all" and stop.type != stop_type_filter:
                continue

            next_stops_data = {}
            for rs in stop.routestop_set.all():
                if rs.status == "E":
                    continue
                sid = rs.stop.id
                if sid not in next_stops_data:
                    next_stops_data[sid] = {
                        "id": sid,
                        "name": rs.stop.title,
                        "routes": []
                    }
                next_stops_data[sid]["routes"].append({
                    "id": rs.route.id,
                    "route": rs.route.number
                })

            result.append({
                "stop_id": stop.id,
                "stop_type": stop.type,
                "stop_name": stop.title,
                "stop_dist": float(stop.distance),
                "next_stop": list(next_stops_data.values()),
                "transports": []
            })

        return result

    def get_nearest_transports(self, user_id: int, lat: Decimal, lon: Decimal) -> List[NearestTransportOut]:
        return self.transport_network_repo.get_nearest_transports(user_id, lat, lon)

    def get_stop_info(self, stop_info_data: StopInfoIn) -> Optional[StopInfoOut]:
        return self.transport_network_repo.get_stop_info(stop_info_data)
