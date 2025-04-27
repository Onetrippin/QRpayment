from typing import List
from http import HTTPStatus

from ninja import Router

from app.internal.common.response_entities import ErrorResponse
from app.internal.past_rides.domain.entities.past_ride import PastRideOut, AddedPastRideOut
from app.internal.past_rides.presentation.rest.handlers import PastRideHandlers


def get_past_rides_router(past_ride_handlers: PastRideHandlers) -> Router:
    router = Router(tags=['past_rides'])

    router.add_api_operation(
        '/past_rides',
        ['POST'],
        past_ride_handlers.add_past_ride,
        response={HTTPStatus.CREATED: AddedPastRideOut, HTTPStatus.BAD_REQUEST: ErrorResponse},
        summary='Записать новую поездку в БД',
    )

    router.add_api_operation(
        '/past_rides',
        ['GET'],
        past_ride_handlers.get_past_rides,
        response={HTTPStatus.OK: List[PastRideOut], HTTPStatus.BAD_REQUEST: ErrorResponse},
        summary='Получить историю поездок',
    )

    return router
