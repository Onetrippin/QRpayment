from django.contrib import admin

from app.internal.transport_network.data.models.transport import Transport


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'garage_number', 'type', 'city', 'route', 'state_number')
    list_filter = ('city__name', 'type')
    search_fields = ('state_number', 'route__title')
