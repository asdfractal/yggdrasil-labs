import stripe
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.conf import settings

from cart.contexts import get_cart_items
from products.models import Product
from profiles.models import UserProfile
from .forms import OrderFormShipping, OrderFormNoShipping


def checkout(request):
    """
    Display a view to purchase items in cart.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = get_cart_items(request)
    cart_total = cart["cart_total"]
    stripe_total = round(cart_total * 100)
    stripe.api_key = stripe_secret_key
    stripe_intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency=settings.STRIPE_CURRENCY,
    )
    print(stripe_intent)
    form = OrderFormNoShipping()

    context = {
        "form": form,
        "stripe_public_key": stripe_public_key,
        "client_secret": stripe_intent.client_secret,
    }

    return render(request, "checkout/checkout.html", context)
