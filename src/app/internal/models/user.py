import uuid

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=32, unique=True)
    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=32, blank=True, null=True, db_index=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    last_ip = models.GenericIPAddressField(blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.chat_id}:{self.last_ip}'

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4().hex
        super().save(*args, **kwargs)
