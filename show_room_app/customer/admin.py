from django.contrib import admin

from customer.models import Customer, Transaction


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "balance",
        "max_price",
        "transaction",
        "is_active",
        "user",
    )
    list_filter = ("username",)
    readonly_fields = ("user",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "car",
        "car_showroom",
        "discount",
        "season_discount",
        "price",
        "date",
    )
    list_filter = ("date",)
    readonly_fields = ("date",)
