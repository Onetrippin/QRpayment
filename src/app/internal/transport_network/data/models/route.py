from django.db import models


class Route(models.Model):
    TRANSPORT_TYPE_CHOICES = [('bus', 'Автобус'), ('trol', 'Троллейбус'), ('tram', 'Трамвай')]

    id = models.AutoField(primary_key=True)
    r_id = models.IntegerField(db_index=True)
    number = models.CharField(max_length=64, db_index=True)
    title = models.TextField(db_index=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    stops = models.ManyToManyField('Stop', through='RouteStop')
    transport_type = models.CharField(choices=TRANSPORT_TYPE_CHOICES, db_index=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return f'{self.r_id}:{self.title}'
