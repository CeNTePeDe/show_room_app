from django.contrib import admin

from car_showroom.models import CarShowRoom, SellModel


class SellModelInLine(admin.TabularInline):
    model = SellModel
    extra = 1


class CarShowRoomAdmin(admin.ModelAdmin):
    inlines = (SellModelInLine,)


class ProviderAdmin(admin.ModelAdmin):
    inlines = (SellModelInLine,)


admin.site.register(CarShowRoom, CarShowRoomAdmin)
