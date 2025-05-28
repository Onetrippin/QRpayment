from django.contrib import admin

from app.internal.transport_network.data.models.stop import Stop


@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('id', 's_id', 'title', 'city', 'latitude', 'longitude')
    list_filter = ('city',)
    search_fields = ('title',)
