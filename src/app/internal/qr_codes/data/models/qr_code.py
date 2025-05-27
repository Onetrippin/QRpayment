from django.db import models


class QRCode(models.Model):
    id = models.AutoField(primary_key=True)
    pay_tag_id = models.BigIntegerField(db_index=True)
    transport = models.ForeignKey('Transport', related_name='qr_codes', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_actual = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'QR code'
        verbose_name_plural = 'QR codes'

    def __str__(self):
        return f'{self.pay_tag_id}'
