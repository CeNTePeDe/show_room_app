from django.contrib import admin

from discount.models import ProviderDiscount, CarShowRoomDiscount, TemporaryDiscount


@admin.register(ProviderDiscount)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("discount_name", "discount_rate")


@admin.register(CarShowRoomDiscount)
class CarShowRoomAdmin(admin.ModelAdmin):
    list_display = ("discount_name", "discount_rate")


@admin.register(TemporaryDiscount)
class TemporaryDiscountAdmin(admin.ModelAdmin):
    list_display = ("discount_name", "discount_rate")
