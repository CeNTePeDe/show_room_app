from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "date_joined",
        "is_customer",
        "is_car_showroom",
        "is_provider",
    )

    list_filter = ("is_customer", "is_car_showroom", "is_provider")
