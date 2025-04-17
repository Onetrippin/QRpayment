from django.db import models


class Stop(models.Model):
    id = models.AutoField(primary_key=True)
    s_id = models.IntegerField(db_index=True)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    title = models.CharField(max_length=64, db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = 'Stop'
        verbose_name_plural = 'Stops'

    def __str__(self):
        return f'{self.id}:{self.title}'
