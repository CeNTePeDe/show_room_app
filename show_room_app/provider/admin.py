from django.contrib import admin

from provider.models import Provider, CarProvider


class CarProviderInLine(admin.TabularInline):
    model = CarProvider
    extra = 1


class CarAdmin(admin.ModelAdmin):
    inlines = (CarProviderInLine,)


class ProviderAdmin(admin.ModelAdmin):
    inlines = (CarProviderInLine,)
    list_display = (
        "name",
        "is_active",
    )
    list_filter = ("name",)


admin.site.register(Provider, ProviderAdmin)
