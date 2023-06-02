from django.contrib import admin

from discount.models import ProviderDiscount, CarShowRoomDiscount


@admin.register(ProviderDiscount)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        "discount_name",
        "discount_rate",
        "date_start",
        "date_finish",
    )


@admin.register(CarShowRoomDiscount)
class CarShowRoomAdmin(admin.ModelAdmin):
    list_display = (
        "discount_name",
        "discount_rate",
        "date_start",
        "date_finish",
    )
