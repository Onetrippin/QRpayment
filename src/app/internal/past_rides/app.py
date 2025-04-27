from ninja import NinjaAPI

from app.internal.past_rides.data.repositories.past_ride import PastRideRepository
from app.internal.past_rides.domain.services.past_ride import PastRideService
from app.internal.past_rides.presentation.rest.handlers import PastRideHandlers
from app.internal.past_rides.presentation.rest.routers import get_past_rides_router


def add_past_rides_router(api: NinjaAPI, path: str) -> None:
    past_ride_repo = PastRideRepository()
    past_ride_service = PastRideService(past_ride_repo=past_ride_repo)
    past_ride_handlers = PastRideHandlers(past_ride_service=past_ride_service)

    past_rides_router = get_past_rides_router(past_ride_handlers)
    api.add_router(path, past_rides_router)
