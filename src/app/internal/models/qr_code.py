from django.db import models


class QRCode(models.Model):
    id = models.AutoField(primary_key=True)
    pay_tag_id = models.BigIntegerField(db_index=True)
    transport = models.ForeignKey('Transport', on_delete=models.CASCADE)
    is_actual = models.BooleanField(default=True, db_index=True)

    class Meta:
        verbose_name = 'QR code'
        verbose_name_plural = 'QR codes'

    def __str__(self):
        return self.pay_tag_id
