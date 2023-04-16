from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "model_car",
        "price",
        "slug",
        "country",
        "created_at",
        "color",
        "engine_type",
        "number_of_doors",
        "is_active",
    ]
    list_filter = ["name", "model_car"]
