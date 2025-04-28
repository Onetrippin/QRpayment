from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.id}: {self.name}'
