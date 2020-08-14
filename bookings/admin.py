from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ("order",)

    fields = (
        "order",
        "user_profile",
        "booking_time",
    )

    list_display = (
        "order",
        "user_profile",
        "booking_time",
    )


admin.site.register(Booking, BookingAdmin)
