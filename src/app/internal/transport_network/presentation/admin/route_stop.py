from django.contrib import admin

from app.internal.transport_network.data.models.route_stop import RouteStop


@admin.register(RouteStop)
class RouteStopAdmin(admin.ModelAdmin):
    list_display = ('route', 'stop', 'status')
    list_filter = ('status',)
    search_fields = ('route__title', 'stop__title')
