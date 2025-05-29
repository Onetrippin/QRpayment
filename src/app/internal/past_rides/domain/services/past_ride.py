from typing import List

from app.internal.past_rides.domain.entities.past_ride import AddedPastRideOut, PastRideIn, PastRideOut
from app.internal.past_rides.domain.interfaces.past_ride import IPastRideRepository


class PastRideService:
    def __init__(self, past_ride_repo: IPastRideRepository) -> None:
        self.past_ride_repo = past_ride_repo

    def get_past_rides(self, user_id: int) -> List[PastRideOut]:
        return self.past_ride_repo.get_past_rides(user_id=user_id)

    def add_past_ride(self, user_id: int, past_ride_data: PastRideIn) -> AddedPastRideOut:
        return self.past_ride_repo.add_past_ride(user_id, past_ride_data)
