from django.db.models.signals import post_save
from django.dispatch import receiver

from checkout.models import Order
from .models import Booking


@receiver(post_save, sender=Order)
def create_booking(sender, instance, created, **kwargs):
    """
    Create new booking when new order created.
    """
    if created:
        Booking.objects.create(order=instance)
