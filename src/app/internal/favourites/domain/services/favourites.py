from datetime import datetime, timedelta

from app.internal.common.response_entities import SuccessResponse
from app.internal.favourites.domain.entities.favourites import SetFavouriteRouteIn, SetFavouriteRouteOut
from app.internal.favourites.domain.interfaces.favourites import IFavouritesRepository


class FavouritesService:
    def __init__(self, favourites_repo: IFavouritesRepository) -> None:
        self.favourites_repo = favourites_repo

    def get_enabled_notifs(self, chat_id: int) -> list[dict]:
        return self.favourites_repo.get_enabled_notifs(chat_id)

    def disable_all_notifs(self, chat_id: int) -> None:
        self.favourites_repo.disable_all_notifs(chat_id)

    def set_favourite_route(self, user_id: int, data: SetFavouriteRouteIn) -> SetFavouriteRouteOut:
        favourite = self.favourites_repo.get_or_create_favourite_route(user_id, data.route_id)

        notifications_data = []
        for notif in data.notifications:
            notifications_data.append({
                'number': notif.number,
                'stop_id': notif.stop_id,
                'days': notif.days,
                'start': datetime.strptime(notif.start, "%H:%M").time(),
                'end': datetime.strptime(notif.end, "%H:%M").time(),
                'interval': timedelta(minutes=notif.interval)
            })

        self.favourites_repo.update_notifications(user_id, favourite.id, notifications_data)

        route = self.favourites_repo.get_route_info(data.route_id)

        return SetFavouriteRouteOut(
            route_id=route.id,
            transport_type=route.transport_type,
            route_number=route.number,
            route_title=route.title,
            price=route.price,
            notice_number=len(notifications_data)
        )


    def delete_favourite_route(self, user_id: int, route_id: int):
        self.favourites_repo.delete_favourite_route(user_id, route_id)
        return SuccessResponse(success=True)