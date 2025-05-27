import uuid

from django.db import models


class Transport(models.Model):
    TRANSPORT_TYPE_CHOICES = [('bus', 'Автобус'), ('trol', 'Троллейбус'), ('tram', 'Трамвай')]

    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=32, unique=True, default='123')
    garage_number = models.CharField(max_length=128, db_index=True)
    type = models.CharField(choices=TRANSPORT_TYPE_CHOICES, db_index=True)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    route = models.ForeignKey('Route', on_delete=models.PROTECT, related_name='transports')
    state_number = models.CharField(max_length=128, db_index=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Transport'
        verbose_name_plural = 'Transports'

    def __str__(self):
        return f'{self.id}:{self.garage_number}'
