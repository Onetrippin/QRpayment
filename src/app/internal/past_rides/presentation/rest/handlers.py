from ninja import Body

from app.internal.past_rides.domain.entities.past_ride import PastRideIn
from app.internal.past_rides.domain.services.past_ride import PastRideService


class PastRideHandlers:
    def __init__(self, past_ride_service: PastRideService) -> None:
        self.past_ride_service = past_ride_service

    def add_past_ride(self, request, past_ride_data: PastRideIn = Body(...)):
        user_id = request.user_id
        return self.past_ride_service.add_past_ride(user_id, past_ride_data)

    def get_past_rides(self, request):
        user_id = request.user_id
        return self.past_ride_service.get_past_rides(user_id)
