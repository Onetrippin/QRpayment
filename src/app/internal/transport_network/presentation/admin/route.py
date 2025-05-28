from django.contrib import admin

from app.internal.transport_network.data.models.route import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'r_id', 'number', 'title', 'city')
    list_filter = ('city',)
    search_fields = ('number', 'title')
