from django.db import models

from profiles.models import UserProfile
from checkout.models import Order


class Booking(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.SET_NULL, null=True, blank=True, related_name="booking"
    )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )
    booking_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.order.order_number
