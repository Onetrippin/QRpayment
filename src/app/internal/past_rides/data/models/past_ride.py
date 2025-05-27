from django.db import models


class PastRide(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    transport = models.ForeignKey('Transport', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Past ride'
        verbose_name_plural = 'Past rides'

    def __str__(self):
        return f'{self.user.username}:{self.transport.garage_number}-{self.date}'
