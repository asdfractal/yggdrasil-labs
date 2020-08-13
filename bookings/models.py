from django.db import models

from profiles.models import UserProfile


class Booking(models.Model):
    booking_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )
    booking_time = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.booking_number
