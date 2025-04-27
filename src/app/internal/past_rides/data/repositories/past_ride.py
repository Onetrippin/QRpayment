from typing import List

from app.internal.past_rides.data.models.past_ride import PastRide
from app.internal.past_rides.domain.entities.past_ride import AddedPastRideOut, PastRideIn, PastRideOut
from app.internal.past_rides.domain.interfaces.past_ride import IPastRideRepository


class PastRideRepository(IPastRideRepository):
    def get_past_rides(self, user_id: int) -> List[PastRideOut]:
        past_rides = (
            PastRide.objects.filter(user_id=user_id)
            .select_related('transport', 'transport__route')
            .values(
                'date',
                'price',
                'transport__state_number',
                'transport__type',
                'transport__route__number',
                'transport__route__name',
            )
            .order_by('-date')
        )
        return [
            PastRideOut(
                route_number=past_ride.get('transport__route__number'),
                route_name=past_ride.get('transport__route__name'),
                transport_type=past_ride.get('transport__type'),
                transport_state_number=past_ride.get('transport_state_number'),
                price=past_ride.get('price'),
                date=past_ride.get('date'),
            )
            for past_ride in past_rides
        ]

    def add_past_ride(self, user_id: int, past_ride_data: PastRideIn) -> AddedPastRideOut:
        created_past_ride = PastRide.objects.create(
            user_id=user_id, transport_id=past_ride_data.transport_id, price=past_ride_data.price
        )
        return AddedPastRideOut(
            user_id=created_past_ride.user_id,
            transport_id=created_past_ride.transport_id,
            price=created_past_ride.price,
        )
