from django.shortcuts import render, get_object_or_404
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile
from .forms import OrderFormShipping, OrderFormNoShipping


def checkout(request):
    """
    Display a view to purchase items in cart.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    client_secret = "test_client"

    form = OrderFormNoShipping()

    context = {
        "form": form,
        "stripe_public_key": stripe_public_key,
        "client_secret": client_secret,
    }

    return render(request, "checkout/checkout.html", context)
