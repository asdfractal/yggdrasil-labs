import uuid
from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    state = models.CharField(max_length=80, null=False, blank=False)
    country = CountryField(blank_label="Country (required)", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    booking_required = models.BooleanField(default=False)
    shipping_required = models.BooleanField(default=False)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default="")

    @staticmethod
    def _generate_order_number():
        """
        Generate an order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.total_price = self.lineitems.aggregate(Sum("total"))["total__sum"] or 0
        self.save()

    def set_booking_required(self):
        for item in self.lineitems.all():
            if item.product.booking_required:
                self.booking_required = True
                self.save()
                break

            self.booking_required = False
            self.save()

    def set_shipping_required(self):
        for item in self.lineitems.all():
            if item.product.shipping_required:
                self.shipping_required = True
                self.save()
                break

            self.shipping_required = False
            self.save()

    def check_complete_create_booking(self, *args, **kwargs):
        if self.stripe_pid:
            if self.booking_required:
                from bookings.models import Booking

                Booking.objects.create(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Set the order number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False,
        default=0,
    )

    def save(self, *args, **kwargs):
        """
        Set the lineitem total and update the order total.
        """
        self.total = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.product.sku} on order {self.order.order_number}"
