from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """
    Display users shopping cart.
    """

    return render(request, "cart/cart.html")


def add_to_cart(request, product_id):
    """
    Add a specified product to the cart.
    """
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get("cart", {})

    if product_id in list(cart.keys()):
        messages.info(request, "That item is already in your cart.")
        print("already in cart")
        return redirect("product_detail", product_id)

    cart[product_id] = 1
    messages.success(request, f"Added {product.name} to your cart.")
    print("added to cart")
    request.session["cart"] = cart
    return redirect("product_detail", product_id)
