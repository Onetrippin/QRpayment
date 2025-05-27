from django.contrib import admin

from app.internal.qr_codes.data.models.qr_code import QRCode

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'pay_tag_id', 'transport', 'price', 'is_actual')
    list_filter = ('is_actual',)
    search_fields = ('transport__state_number',)
