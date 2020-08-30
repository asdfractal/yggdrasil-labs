from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Display and modify products in admin panel.
    """

    list_display = (
        "sku",
        "name",
        "category",
        "booking_required",
        "shipping_required",
        "price",
    )
    ordering = ["sku"]


class CategoryAdmin(admin.ModelAdmin):
    """
    Display and modify categories in admin panel.
    """

    list_display = ("name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
