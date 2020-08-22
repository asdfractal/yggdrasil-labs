from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    # readonly_fields = ("order",)

    list_display = (
        "order",
        "user_profile",
        "booking_date",
        "booking_time",
    )


admin.site.register(Booking, BookingAdmin)
