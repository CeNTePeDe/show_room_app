from django.contrib import admin

from car_showroom.models import CarShowRoom, SellModel


class SellModelInLine(admin.TabularInline):
    model = SellModel
    extra = 1


class CarShowRoomAdmin(admin.ModelAdmin):
    inlines = (SellModelInLine,)
    list_display = (
        "name",
        "country",
        "balance",
        "user",
        "is_active",
        )
    list_filter = ("name",)


class ProviderAdmin(admin.ModelAdmin):
    inlines = (SellModelInLine,)


admin.site.register(CarShowRoom, CarShowRoomAdmin)
