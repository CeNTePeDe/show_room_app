from django.contrib import admin

from customer.models import Customer, Transaction


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "balance",
        "model_car",
        "is_active",
        "user",
    )
    list_filter = ("username",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "car",
        "car_showroom",
        "customer",
        "price",
        "date",
    )
    list_filter = ("date",)
    readonly_fields = ("date",)
