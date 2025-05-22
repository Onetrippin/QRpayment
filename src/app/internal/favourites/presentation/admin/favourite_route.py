from django.contrib import admin

from app.internal.favourites.data.models.favourite_route import FavouriteRoute


@admin.register(FavouriteRoute)
class FavouriteRouteAdmin(admin.ModelAdmin):
    list_display = ('user', 'route', 'notifications_enabled')
    list_filter = ('notifications_enabled',)
    search_fields = ('user__username', 'route__title')