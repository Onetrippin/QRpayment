from decimal import Decimal, getcontext
from typing import Optional, List

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Case, IntegerField, Q, When

from django.db.models import ExpressionWrapper, DecimalField, F, Prefetch, QuerySet
from django.db.models.functions import ATan2, Sqrt, Sin, Radians, Cos

from app.internal.cities.data.models.city import City
from app.internal.favourites.data.models.favourite_route import FavouriteRoute
from app.internal.qr_codes.data.models.qr_code import QRCode
from app.internal.transport_network.data.models.route_stop import RouteStop
from app.internal.transport_network.data.models.stop import Stop
from app.internal.transport_network.data.models.transport import Transport
from app.internal.transport_network.domain.entities.transport_network import (
    PaymentTransportInfoIn,
    PaymentTransportInfoOut,
    StopInfoIn,
    StopInfoOut,
    NextStopInfo,
    StopTransportInfo,
    NearestTransportOut,
    StopRouteOut,
)
from app.internal.transport_network.domain.interfaces.transport_network import ITransportNetworkRepository


getcontext().prec = 6


class TransportNetworkRepository(ITransportNetworkRepository):
    def get_transport(self, city: str, query: str, offset: int, limit: int = 51) -> list[dict]:
        filters = Q(city__name__iexact=city) & (Q(route__number__icontains=query) | Q(state_number__icontains=query))

        if query:
            order = [
                Case(
                    When(route__number__icontains=query, then=0),
                    When(state_number__icontains=query, then=1),
                    default=2,
                    output_field=IntegerField(),
                )
            ]
        else:
            order = []

        return list(
            (
                Transport.objects.filter(filters)
                .select_related('route', 'city')
                .annotate(
                    pay_tag_ids=ArrayAgg('qr_codes__pay_tag_id', filter=Q(qr_codes__is_actual=True), distinct=True)
                )
                .values(
                    'type',
                    'state_number',
                    'route__number',
                    'route__title',
                    'pay_tag_ids',
                )
            ).order_by(*order, 'route__number', 'state_number')[offset : offset + limit]
        )

    def get_stops_within_radius(
            self,
            latitude: Decimal,
            longitude: Decimal,
            radius_km: Decimal = Decimal("1.0")
    ) -> QuerySet[Stop]:
        R = Decimal("6371.0")
        distance_expr = ExpressionWrapper(
            R * 2 * ATan2(
                Sqrt(
                    Sin(Radians(F("latitude") - latitude) / 2) ** 2
                    + Cos(Radians(latitude)) * Cos(Radians(F("latitude")))
                    * Sin(Radians(F("longitude") - longitude) / 2) ** 2
                ),
                Sqrt(1 - (
                        Sin(Radians(F("latitude") - latitude) / 2) ** 2
                        + Cos(Radians(latitude)) * Cos(Radians(F("latitude")))
                        * Sin(Radians(F("longitude") - longitude) / 2) ** 2
                ))
            ),
            output_field=DecimalField(),
            )

        qs = Stop.objects.annotate(distance=distance_expr).filter(distance__lte=radius_km)
        qs = qs.prefetch_related(
            "routestop_set__route__transports",
        )

        return qs

    def get_nearest_transports(self, user_id: int, lat: Decimal, lon: Decimal) -> List[NearestTransportOut]:
        transports = (
            Transport.objects.filter(city__in=City.objects.filter(user__id=user_id))
            .select_related("route")
            .prefetch_related("qr_codes", "route__favourited_by")
        )

        result = []
        for transport in transports:
            is_favourite = FavouriteRoute.objects.filter(user_id=user_id, route=transport.route).exists()
            qr_code = transport.qr_codes.filter(is_actual=True).first()
            price = qr_code.price if qr_code else 0

            transport_type_map = {
                1: "Автобус",
                2: "Троллейбус",
                3: "Трамвай",
            }
            transport_type = transport_type_map.get(transport.type, "Неизвестный")

            arrival_time = 300

            current_stop = "Текущая остановка"
            next_stop = "Следующая остановка"

            result.append(
                NearestTransportOut(
                    transport_uuid=str(transport.uuid),
                    transport_type=transport_type,
                    route_number=transport.route.number,
                    state_number=transport.state_number,
                    route_title=transport.route.title,
                    route_id=transport.route.id,
                    current_stop=current_stop,
                    next_stop=next_stop,
                    is_favourite=is_favourite,
                    price=price,
                    arrival_time=arrival_time,
                )
            )

        return result

    def get_transport_info(self, transport_info_data: PaymentTransportInfoIn, user_id: int, user_uuid: str) -> Optional[
        PaymentTransportInfoOut]:
        try:
            transport = (
                Transport.objects
                .select_related("route", "city")
                .prefetch_related("qr_codes", "route__favourited_by")
                .get(uuid=transport_info_data.transport_uuid)
            )
        except Transport.DoesNotExist:
            return None

        qr_codes = transport.qr_codes.filter(is_actual=True)
        price = qr_codes.first().price if qr_codes.exists() else 0

        paytagid_list = [
            {"id": qr.id, "pay_tag_id": qr.pay_tag_id}
            for qr in qr_codes
        ]

        is_favourite = FavouriteRoute.objects.filter(user_id=user_id, route=transport.route).exists()

        transport_type = {
            1: "Автобус",
            2: "Троллейбус",
            3: "Трамвай",
        }.get(transport.type, "Неизвестный")

        return PaymentTransportInfoOut(
            route_number=transport.route.number,
            route_title=transport.route.title,
            route_id=transport.route.id,
            transport_type=transport_type,
            state_number=transport.state_number,
            price=price,
            is_favourite=is_favourite,
            current_stop="В процессе...",
            next_stop="В процессе...",
            user_uuid=user_uuid,
            paytagid=paytagid_list
        )

    def get_stop_info(self, stop_info_data: StopInfoIn) -> Optional[StopInfoOut]:
        try:
            stop = Stop.objects.prefetch_related(
                Prefetch(
                    'routestop_set',
                    queryset=RouteStop.objects.select_related('route')
                ),
                Prefetch(
                    'route_set__transports',
                    queryset=Transport.objects.prefetch_related(
                        Prefetch('qr_codes', queryset=QRCode.objects.filter(is_actual=True))
                    ).select_related('route')
                )
            ).get(id=stop_info_data.stop_id)
        except Stop.DoesNotExist:
            return None

        transport_types = {
            1: "Автобусная",
            2: "Троллейбусная",
            3: "Трамвайная"
        }
        stop_routes = stop.route_set.all()
        transport_type_set = {transport_types.get(t.type, "Неизвестная") for r in stop_routes for t in
                              r.transports.all()}
        stop_type = ", ".join(transport_type_set)

        next_stops_map = {}
        for rs in stop.routestop_set.all():
            if rs.status == 'E':
                continue

            route = rs.route

            next_rs = RouteStop.objects.filter(
                route=route,
                id__gt=rs.id,
            ).select_related('stop').exclude(status='E').first()

            if next_rs:
                ns_id = next_rs.stop.id
                if ns_id not in next_stops_map:
                    next_stops_map[ns_id] = {
                        "name": next_rs.stop.title,
                        "routes": []
                    }
                next_stops_map[ns_id]["routes"].append(
                    StopRouteOut(id=route.id, route=route.title)
                )

        next_stops = [
            NextStopInfo(id=stop_id, name=data["name"], routes=data["routes"])
            for stop_id, data in next_stops_map.items()
        ]

        transports_list = []
        added_transports = set()
        for route in stop_routes:
            for transport in route.transports.all():
                if transport.id in added_transports:
                    continue
                added_transports.add(transport.id)

                qr = next((q for q in transport.qr_codes.all() if q.is_actual), None)
                transports_list.append(
                    StopTransportInfo(
                        transport_uuid=transport.uuid,
                        transport_type=transport_types.get(transport.type, "Неизвестный"),
                        route_number=transport.route.number,
                        state_number=transport.state_number,
                        route_title=transport.route.title,
                        price=qr.price if qr else 0,
                        arrival_time=0  # заглушка
                    )
                )

        return StopInfoOut(
            stop_type=stop_type,
            stop_name=stop.title,
            next_stops=next_stops,
            transports=transports_list
        )
