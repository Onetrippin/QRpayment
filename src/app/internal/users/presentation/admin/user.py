from django.contrib import admin

from app.internal.users.data.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'username', 'first_name',
                    'last_ip', 'city', 'created_at')
    list_filter = ('city', 'created_at')
    search_fields = ('username', 'first_name', 'last_name')