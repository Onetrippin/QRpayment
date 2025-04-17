from django.db import models


class RouteStop(models.Model):
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    stop = models.ForeignKey('Stop', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, db_index=True, default='')

    class Meta:
        verbose_name = 'RouteStop'
        verbose_name_plural = 'RouteStops'

    def __str__(self):
        return f'{self.route}:{self.stop} ({self.status})'
