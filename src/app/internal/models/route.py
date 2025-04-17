from django.db import models


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    r_id = models.IntegerField(db_index=True)
    number = models.CharField(max_length=64, db_index=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    stops = models.ManyToManyField('Stop', through='RouteStop')

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return f'{self.id}:{self.r_id}'
