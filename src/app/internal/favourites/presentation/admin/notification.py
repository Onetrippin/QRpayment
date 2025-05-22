from django.contrib import admin

from app.internal.favourites.data.models.notification import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'favourite_route', 'stop')
    search_fields = ('user__username', 'favourite_route__route__title', 'stop__title')
    ordering = ('id',)