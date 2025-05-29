from django.contrib import admin

from app.internal.cities.presentation.admin.city import CityAdmin
from app.internal.favourites.presentation.admin.favourite_route import FavouriteRouteAdmin
from app.internal.favourites.presentation.admin.notification import NotificationAdmin
from app.internal.past_rides.presentation.admin.past_ride import PastRideAdmin
from app.internal.qr_codes.presentation.admin.qr_code import QRCodeAdmin
from app.internal.transport_network.presentation.admin.route import RouteAdmin
from app.internal.transport_network.presentation.admin.route_stop import RouteStopAdmin
from app.internal.transport_network.presentation.admin.stop import StopAdmin
from app.internal.transport_network.presentation.admin.transport import TransportAdmin
from app.internal.users.presentation.admin.admin_user import AdminUserAdmin
from app.internal.users.presentation.admin.user import UserAdmin

admin.site.site_title = 'QR-payment administration'
admin.site.site_header = 'QR-payment administration'
