from abc import ABC, abstractmethod
from typing import List

from app.internal.past_rides.domain.entities.past_ride import AddedPastRideOut, PastRideIn, PastRideOut


class IPastRideRepository(ABC):
    @abstractmethod
    def get_past_rides(self, user_id: int) -> List[PastRideOut]:
        ...

    @abstractmethod
    def add_past_ride(self, user_id: int, past_ride_data: PastRideIn) -> AddedPastRideOut:
        ...
