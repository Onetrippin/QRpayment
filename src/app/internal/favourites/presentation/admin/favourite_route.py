from django.contrib import admin

from app.internal.favourites.data.models.favourite_route import FavouriteRoute


@admin.register(FavouriteRoute)
class FavouriteRouteAdmin(admin.ModelAdmin):
    list_display = ('user', 'route')
    search_fields = ('user__username', 'route__title')
