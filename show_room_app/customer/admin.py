from django.contrib import admin

from customer.models import Customer, Transaction


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "balance",
        "purchases",
        "max_price",
        "is_active",
        "user",
    )
    list_filter = ("username",)
    readonly_fields = ("user",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "car_showroom",
        "price",
        "discount",
        "season_discount",
        "date",
    )
    list_filter = ("date",)
    readonly_fields = ("date",)
