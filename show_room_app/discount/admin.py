from django.contrib import admin

from discount.models import ProviderDiscount, CarShowRoomDiscount


@admin.register(ProviderDiscount)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(CarShowRoomDiscount)
class CarShowRoomAdmin(admin.ModelAdmin):
    pass
