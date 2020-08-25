import json
import time

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem


class StripeWebhookHandler:
    """
    Handle Stripe webhooks.
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic webhook event.
        """
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment intent succeeeded webhook event.
        """
        intent = event.data.object
        pid = intent.id
        cart = json.loads(intent.metadata.cart)
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        total_price = round(intent.charges.data[0].amount / 100, 2)
        user_profile = UserProfile.objects.get(user__username=intent.metadata.username)

        if shipping_details:
            for key, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[key] = None
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    state__iexact=shipping_details.address.state,
                    country__iexact=shipping_details.address.country,
                    total_price=total_price,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]}. Verified order in database',
                status=200,
            )

        order = None
        try:
            order = Order.objects.create(
                full_name=shipping_details.name,
                user_profile=user_profile,
                email=billing_details.email,
                phone_number=shipping_details.phone,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                postcode=shipping_details.address.postal_code,
                city=shipping_details.address.city,
                state=shipping_details.address.state,
                country=shipping_details.address.country,
                total_price=total_price,
                stripe_pid=pid,
            )
            for key in list(cart.keys()):
                product = get_object_or_404(Product, pk=key)
                order_line_item = OrderLineItem(order=order, product=product)
                order_line_item.save()
        except Exception as e:
            if order:
                order.delete()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Error: {e}', status=500,
            )
        return HttpResponse(
            content=f'Webhook received: {event["type"]}. Created order in webhook',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment intent payment failed webhook event.
        """
        return HttpResponse(
            content=f'Payment intent payment failed webhook received: {event["type"]}',
            status=200,
        )
