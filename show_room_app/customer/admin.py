from django.contrib import admin

from customer.models import Customer, Transaction


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "slug",
        "balance",
        "max_price",
        "is_active",
        "purchases",
    )
    list_filter = ("username",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("car_showroom", "price", "discount", "date")
    list_filter = ("date",)
