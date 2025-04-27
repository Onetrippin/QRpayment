from datetime import timedelta

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Notification(models.Model):
    WEEK_DAYS = [
        ('mon', 'ПН'),
        ('tue', 'ВТ'),
        ('wed', 'СР'),
        ('thu', 'ЧТ'),
        ('fri', 'ПТ'),
        ('sat', 'СБ'),
        ('sun', 'ВС'),
    ]

    INTERVALS = [
        (timedelta(minutes=5), '5'),
        (timedelta(minutes=10), '10'),
        (timedelta(minutes=15), '15'),
        (timedelta(minutes=20), '20'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', related_name='notifications', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    favourite_route = models.ForeignKey('FavouriteRoute', on_delete=models.CASCADE)
    stop = models.ForeignKey('Stop', related_name='notifications_stops', on_delete=models.CASCADE)
    days = ArrayField(models.CharField(max_length=15, choices=WEEK_DAYS))
    time_from = models.TimeField()
    time_to = models.TimeField()
    interval = models.DurationField(choices=INTERVALS)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        constraints = [models.UniqueConstraint(fields=['user', 'number'], name='uniq_number_per_user')]

    def __str__(self):
        return f'{self.id}:{self.user}'
