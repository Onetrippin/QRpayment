from http import HTTPStatus

from ninja import Router

from app.internal.common.response_entities import SuccessResponse
from app.internal.favourites.domain.entities.favourites import SetFavouriteRouteOut, SetFavouriteRouteIn
from app.internal.favourites.presentation.rest.handlers import FavouritesHandlers


def get_favourites_router(favourites_handlers: FavouritesHandlers) -> Router:
    router = Router(tags=['favourites'])

    @router.post(
        '/favourites/route',
        response={HTTPStatus.OK: SetFavouriteRouteOut},
        summary='Добавление или обновление маршрута в избранное',
    )
    def set_favourite(request, data: SetFavouriteRouteIn):
        user_id = request.user.id
        return favourites_handlers.set_favourite_route(user_id, data)

    @router.delete(
        '/favourites/route/{route_id}',
        response={HTTPStatus.OK: SuccessResponse},
        summary='Удаление маршрута из избранного'
    )
    def delete_favourite_route(request, route_id: int):
        user_id = request.user.id
        return favourites_handlers.delete_favourite_route(user_id, route_id)

    return router
