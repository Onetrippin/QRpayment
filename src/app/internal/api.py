from django.urls import path
from ninja import NinjaAPI

from app.internal.cities.app import add_cities_router
from app.internal.common.auth import HTTPJWTAuth
from app.internal.favourites.app import add_favourites_router
from app.internal.past_rides.app import add_past_rides_router
from app.internal.qr_codes.app import add_qrcodes_router
from app.internal.transport_network.app import add_transport_network_router
from app.internal.users.app import add_users_router


def get_api():
    api = NinjaAPI(title='QRpayment', version='1.0.0', auth=[HTTPJWTAuth()])

    add_cities_router(api, '')
    add_favourites_router(api, '')
    add_qrcodes_router(api, '')
    add_past_rides_router(api, '')
    add_transport_network_router(api, '')
    add_users_router(api, '')

    return api


ninja_api = get_api()

urlpatterns = [
    path('', ninja_api.urls),
]
