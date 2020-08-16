from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdmin,)

    readonly_fields = (
        "order_number",
        "date",
        "total_price",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "date",
        "user_profile",
        "full_name",
        "email",
        "phone_number",
        "street_address1",
        "street_address2",
        "city",
        "postcode",
        "state",
        "country",
        "booking_required",
        "shipping_required",
        "total_price",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "booking",
        "date",
        "full_name",
        "total_price",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
