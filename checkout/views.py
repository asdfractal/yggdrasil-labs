import json
import stripe
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.http import require_POST

from yggdrasil_labs.utils.verify_purchase import verify_purchase
from cart.contexts import get_cart_items
from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem
from .forms import OrderForm


@require_POST
def cache_checkout_data(request):
    """
    Save cart and user data in case of processing error.
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "username": request.user,
                "save_info": request.POST.get("save_info"),
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


def checkout_login_check(request):
    """
    Checks if the user is authenticated before rendering the checkout view in order
    to display a message informing them that login is required and utilize allauth
    next url parameter.
    """
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to checkout.")
    return checkout(request)


@login_required
def checkout(request):
    """
    Display a view to purchase items in cart. Checks user has no duplicate products
    and processes Stripe payment.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get("cart", {})
    user_profile = UserProfile.objects.get(user=request.user)
    form = OrderForm()
    duplicate_products = []

    for key in list(cart.keys()):
        product = get_object_or_404(Product, pk=key)
        if verify_purchase(user_profile, Order, product):
            duplicate_products.append(key)

    if len(duplicate_products) != 0:
        for key in duplicate_products:
            if key in list(cart.keys()):
                try:
                    del cart[key]
                    request.session["cart"] = cart
                except KeyError:
                    messages.error(
                        request, "There was an error with an item in your cart.",
                    )
                    return redirect("view_cart")
        messages.warning(
            request,
            "You had an item in your cart that you have already purchased. It was removed.",
            extra_tags="cart_remove",
        )
        return redirect("view_cart")

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.stripe_pid = request.POST.get("client_secret").split("_secret")[0]
            order.user_profile = user_profile
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
            order.check_complete_create_booking(order=order, user_profile=user_profile)
            user_profile.is_client = True
            user_profile.check_personal_key()
            request.session["save_info"] = "save-info" in request.POST
            messages.success(request, "Order placed successfully")
            return redirect(reverse("checkout_success", args=[order.order_number]))
        messages.error(
            request,
            "There is a problem with your form. Please confirm details and submit again.",
        )
        return redirect(reverse("checkout"))

    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect(reverse("products"))
    if request.user.is_authenticated:
        try:
            form = OrderForm(
                initial={
                    "full_name": user_profile.default_full_name,
                    "email": user_profile.user.email,
                    "phone_number": user_profile.default_phone_number,
                    "street_address1": user_profile.default_street_address1,
                    "street_address2": user_profile.default_street_address2,
                    "city": user_profile.default_city,
                    "postcode": user_profile.default_postcode,
                    "state": user_profile.default_state,
                    "country": user_profile.default_country,
                }
            )
        except UserProfile.DoesNotExist:
            form = OrderForm()

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
        "page_title": "Checkout",
    }

    return render(request, "checkout/checkout.html", context)


@login_required
def checkout_success(request, order_number):
    """
    A view confirming successful checkout.
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)
    user_profile = UserProfile.objects.get(user=request.user)

    if "cart" in request.session:
        del request.session["cart"]

    if save_info:
        user_profile.default_full_name = order.full_name
        user_profile.default_phone_number = order.phone_number
        user_profile.default_street_address1 = order.street_address1
        user_profile.default_street_address2 = order.street_address2
        user_profile.default_city = order.city
        user_profile.default_postcode = order.postcode
        user_profile.default_state = order.state
        user_profile.default_country = order.country
        user_profile.save()

    context = {
        "order": order,
        "page_title": "Success",
    }
    return render(request, "checkout/checkout-success.html", context)
