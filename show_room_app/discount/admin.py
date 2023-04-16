from django.contrib import admin

from discount.models import ProviderDiscount, CarShowRoomDiscount

admin.site.register(ProviderDiscount)
admin.site.register(CarShowRoomDiscount)
