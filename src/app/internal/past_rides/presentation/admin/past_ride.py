from django.contrib import admin

from app.internal.past_rides.data.models.past_ride import PastRide


@admin.register(PastRide)
class PastRideAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'transport', 'price', 'date')
    list_filter = ('date',)
    search_fields = ('user__username', 'transport__state_number')