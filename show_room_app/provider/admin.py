from django.contrib import admin

from provider.models import Provider, CarProvider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name_company", "is_active", "characteristic", "country", "year", "slug")
    list_filter = ("name_company",)
    search_fields = ("name_company__startswith",)


@admin.register(CarProvider)
class CarProviderAdmin(admin.ModelAdmin):
    list_display = ("provider", "margin", "car", "number_of_cars")
