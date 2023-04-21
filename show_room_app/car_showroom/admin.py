from django.contrib import admin

from car_showroom.models import CarShowRoom, ProviderCarShowRoom


@admin.register(CarShowRoom)
class CarShowRoomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_active",
        "balance",
        "year",
        "country",
        "characteristic",
    )
    list_filter = (
        "name",
        "is_active",
    )
    search_fields = ("name__startswith",)
    readonly_fields = ("id",)


@admin.register(ProviderCarShowRoom)
class ProviderCarShowRoom(admin.ModelAdmin):
    list_display = (
        "provider",
        "margin",
        "car_showroom",
        "number_of_cars",
        "discount",
    )
