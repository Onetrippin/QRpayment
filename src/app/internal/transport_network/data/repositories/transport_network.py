from typing import Optional

from django.db import models
from django.db.models import OuterRef, Q, Subquery

from app.internal.qr_codes.data.models.qr_code import QRCode
from app.internal.transport_network.data.models.transport import Transport
from app.internal.transport_network.domain.entities.transport_network import TransportInfoIn, TransportInfoOut
from app.internal.transport_network.domain.interfaces.transport_network import ITransportNetworkRepository


class TransportNetworkRepository(ITransportNetworkRepository):
    def get_transport(self, city: str, query: str, offset: int, limit: int = 51) -> list[dict]:
        filters = Q(city__name__iexact=city) & (Q(route__number__icontains=query) | Q(state_number__icontains=query))

        qr_subquery = QRCode.objects.filter(transport=OuterRef('pk'), is_actual=True).values('pay_tag_id')[:1]

        return (
            (
                Transport.objects.filter(filters)
                .select_related('route', 'city')
                .annotate(pay_tag_id=Subquery(qr_subquery))
                .values(
                    'type',
                    'state_number',
                    'route__number',
                    'route__title',
                    'pay_tag_id',
                )
            ).order_by(
                models.Case(
                    models.When(route__number__icontains=query, then=0),
                    models.When(state_number__icontains=query, then=1),
                    default=2,
                    output_field=models.IntegerField(),
                ),
                'route__number',
                'state_number',
            )
        )[offset : offset + limit]

    def get_transport_info(self, transport_info_data: TransportInfoIn) -> Optional[TransportInfoOut]:
        from django.db import connection, reset_queries

        reset_queries()
        transport = (
            Transport.objects.filter(
                state_number=transport_info_data.state_number, route__title=transport_info_data.route_title
            )
            .select_related('route')
            .prefetch_related('qr_codes')
            .values(
                'route__title',
                'route__number',
                'state_number',
                'qr_codes__pay_tag_id',
                'qr_codes__price',
                'qr_codes__is_actual',
            )
            .first()
        )

        if not transport:
            return None

        qr_codes_links = [
            f'https://qr.bilet.nspk.ru/payment?paytagid={pay_tag_id}'
            for pay_tag_id in transport.get('qr_codes__pay_tag_id', [])
            if transport.get('qr_codes__is_actual')
        ]

        return TransportInfoOut(
            route_title=transport['route__title'],
            route_number=transport['route__number'],
            state_number=transport['state_number'],
            current_stop='В процессе...',
            next_stop='В процессе...',
            price=transport.get('qr_codes__price'),
            qr_code_links=qr_codes_links,
        )
