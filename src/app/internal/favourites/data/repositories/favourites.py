from django.db import transaction

from app.internal.favourites.data.models.favourite_route import FavouriteRoute
from app.internal.favourites.data.models.notification import Notification
from app.internal.favourites.domain.interfaces.favourites import IFavouritesRepository
from app.internal.transport_network.data.models.route import Route


class FavouritesRepository(IFavouritesRepository):
    def get_enabled_notifs(self, chat_id: int) -> list[dict]:
        notifs = list(
            Notification.objects.filter(user__chat_id=chat_id, is_enabled=True).values(
                'days',
                'time_from',
                'time_to',
                'favourite_route__route__number',
                'favourite_route__route__title',
                'favourite_route__route__city__name',
                'favourite_route__route__transport_type',
                'stop__title',
            )
        )

        days_choices_map = dict(Notification._meta.get_field('days').base_field.choices)

        for notif in notifs:
            notif['days'] = [days_choices_map.get(day, day) for day in notif['days']]

        return notifs

    def disable_all_notifs(self, chat_id: int) -> None:
        Notification.objects.filter(user__chat_id=chat_id, is_enabled=True).update(is_enabled=False)

    def get_or_create_favourite_route(self, user_id: int, route_id: int):
        with transaction.atomic():
            favourite, created = FavouriteRoute.objects.get_or_create(
                user_id=user_id,
                route_id=route_id,
                defaults={'notifications_enabled': True}
            )
            if created:
                self.create_default_notifications(user_id, favourite.id)
            return favourite

    def create_default_notifications(self, user_id: int, favourite_id: int):
        notifications = [
            Notification(
                user_id=user_id,
                favourite_route_id=favourite_id,
                number=i + 1,  # 1..10
                stop_id=None,
                days=[],
                time_from=None,
                time_to=None,
                interval=None
            )
            for i in range(10)
        ]
        Notification.objects.bulk_create(notifications)

    def update_notifications(self, user_id: int, favourite_id: int, notifications_data: list):
        for notif in notifications_data:
            Notification.objects.filter(
                user_id=user_id,
                favourite_route_id=favourite_id,
                number=notif['number']
            ).update(
                stop_id=notif['stop_id'],
                days=notif['days'],
                time_from=notif['start'],
                time_to=notif['end'],
                interval=notif['interval']
            )

    def get_route_info(self, route_id: int):
        return Route.objects.get(id=route_id)

    def delete_favourite_route(self, user_id: int, route_id: int):
        FavouriteRoute.objects.filter(user_id=user_id, route_id=route_id).delete()