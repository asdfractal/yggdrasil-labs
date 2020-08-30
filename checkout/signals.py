from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total and shipping/booking status on lineitem update/create.
    """
    instance.order.update_total()
    instance.order.set_booking_required()
    instance.order.set_shipping_required()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total and shipping/booking status on lineitem delete.
    """
    instance.order.update_total()
    instance.order.set_booking_required()
    instance.order.set_shipping_required()
