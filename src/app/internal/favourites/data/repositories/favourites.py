from app.internal.favourites.data.models.notification import Notification
from app.internal.favourites.domain.interfaces.favourites import IFavouritesRepository


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
