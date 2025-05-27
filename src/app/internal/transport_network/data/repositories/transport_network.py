from django.db import models
from django.db.models import OuterRef, Q, Subquery

from app.internal.qr_codes.data.models.qr_code import QRCode
from app.internal.transport_network.data.models.transport import Transport
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
