from django.db import models
from django.utils import timezone

from profiles.models import UserProfile
from checkout.models import Order


class Booking(models.Model):
    """
    Booking model for a user to create a booking associated with an order.
    """

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

    @property
    def time_in_future(self):
        """
        A property to check if the booking is in the past or future.
        """
        if self.booking_time:
            return timezone.now() < self.booking_time
        return None

    def __str__(self):
        if self.user_profile:
            return f"Booking for {self.user_profile.default_full_name}"
        return ""
