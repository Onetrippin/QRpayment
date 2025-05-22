from django.db import models


class FavouriteRoute(models.Model):
    user = models.ForeignKey('User', related_name='favourite_routes', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', related_name='favourited_by', on_delete=models.CASCADE)
    notifications_enabled = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Favourite route'
        verbose_name_plural = 'Favourite routes'

    def __str__(self):
        return f'{self.user.username}:{self.route.title}'
