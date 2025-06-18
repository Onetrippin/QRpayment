from app.internal.users.domain.entities.user import TelegramUserIn
from app.internal.cities.data.models.city import City
from app.internal.users.data.models.user import User
from app.internal.users.domain.entities.user import UserCityIn
from app.internal.users.domain.interfaces.user import IUserRepository


class UserRepository(IUserRepository):
    def add_user_if_not_exists(self, user_data: TelegramUserIn) -> None:
        user, created = User.objects.get_or_create(
            chat_id=user_data.chat_id,
            defaults={
                'username': user_data.username,
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
            },
        )
        if not created:
            need_update_fields = []
            for field in ('username', 'first_name', 'last_name'):
                new_value = getattr(user_data, field)
                if new_value and new_value != getattr(user, field):
                    setattr(user, field, new_value)
                    need_update_fields.append(field)
            if need_update_fields:
                user.save(update_fields=need_update_fields)
        return

    def get_city_by_chat_id(self, chat_id: int) -> str | None:
        return User.objects.filter(chat_id=chat_id).values_list('city__name', flat=True).first()

    def set_user_city(self, user_id: int, user_city_data: UserCityIn) -> bool:
        city_exists = City.objects.filter(id=user_city_data.city_id, is_active=True).exists()
        if not city_exists:
            return False

        updated = User.objects.filter(id=user_id).update(city_id=user_city_data.city_id)
        return updated > 0
