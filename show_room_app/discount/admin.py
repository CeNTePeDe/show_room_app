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
    list_filter = ("provider_discount",)


@admin.register(CarShowRoomDiscount)
class CarShowRoomAdmin(admin.ModelAdmin):
    list_display = (
        "discount_name",
        "discount_rate",
        "date_start",
        "date_finish",
    )

    list_filter = ("car_showroom_discount",)
