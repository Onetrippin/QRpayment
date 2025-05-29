from http import HTTPStatus
from typing import List

from ninja import Body, Router

from app.internal.common.response_entities import ErrorResponse
from app.internal.past_rides.domain.entities.past_ride import AddedPastRideOut, PastRideIn, PastRideOut
from app.internal.past_rides.presentation.rest.handlers import PastRideHandlers


def get_past_rides_router(past_ride_handlers: PastRideHandlers) -> Router:
    router = Router(tags=['past_rides'])

    @router.post(
        '/past_rides',
        response={HTTPStatus.CREATED: AddedPastRideOut, HTTPStatus.BAD_REQUEST: ErrorResponse},
        summary='Записать новую поездку в БД',
    )
    def add_past_ride(request, past_ride_data: PastRideIn = Body(...)):
        return past_ride_handlers.add_past_ride(request, past_ride_data)

    @router.get(
        '/past_rides',
        response={HTTPStatus.OK: List[PastRideOut], HTTPStatus.BAD_REQUEST: ErrorResponse},
        summary='Получить историю поездок',
    )
    def get_past_rides(request):
        return past_ride_handlers.get_past_rides(request)

    return router
