import stripe
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings

from cart.contexts import get_cart_items
from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem
from .forms import OrderForm


def checkout(request):
    """
    Display a view to purchase items in cart.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get("cart", {})
    form = OrderForm()

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.user_profile = get_object_or_404(UserProfile, user=request.user)
            order.save()
            for key in list(cart.keys()):
                try:
                    product = get_object_or_404(Product, pk=key)
                    order_line_item = OrderLineItem(order=order, product=product)
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, f"{product} not found.")
                    order.delete()
                    return redirect(reverse("view_cart"))
            return redirect(reverse("checkout_success", args=[order.order_number]))

    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect(reverse("products"))

    current_cart = get_cart_items(request)
    current_total = current_cart["cart_total"]
    stripe_total = round(current_total * 100)
    stripe.api_key = stripe_secret_key
    stripe_intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency=settings.STRIPE_CURRENCY,
    )

    context = {
        "form": form,
        "stripe_public_key": stripe_public_key,
        "client_secret": stripe_intent.client_secret,
    }

    return render(request, "checkout/checkout.html", context)


def checkout_success(request, order_number):
    """
    A view confirming successful checkout.
    """
    context = {
        "order_number": order_number,
    }
    return render(request, "checkout/checkout_success.html", context)
