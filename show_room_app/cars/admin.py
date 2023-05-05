from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "model_car",
        "year",
        "price",
        "country",
        "created_at",
        "body_type",
        "color",
        "engine_type",
        "number_of_doors",
        "is_active",
    )
    list_filter = (
        "name",
        "model_car",
    )
    readonly_fields = ("id",)
