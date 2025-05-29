from django.db import models
from django.db.models import Index, Q


class RouteStop(models.Model):
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    stop = models.ForeignKey('Stop', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='')

    objects = models.Manager()

    class Meta:
        verbose_name = 'RouteStop'
        verbose_name_plural = 'RouteStops'
        indexes = [
            Index(fields=['status'], name='status_b_index', condition=Q(status='B')),
            Index(fields=['status'], name='status_e_index', condition=Q(status='E')),
        ]

    def __str__(self):
        return f'{self.route}:{self.stop} ({self.status})'
