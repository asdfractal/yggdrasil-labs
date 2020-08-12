from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    HttpResponse,
)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """
    Display users shopping cart.
    """
    cart = request.session.get("cart", {})
    cart_items = []
    for key in list(cart.keys()):
        product = get_object_or_404(Product, pk=key)
        cart_items.append(
            {"product": product,}
        )
    context = {
        "cart_items": cart_items,
    }
    return render(request, "cart/cart.html", context)


def add_to_cart(request, product_id):
    """
    Add a specified product to the cart.
    """
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get("cart", {})

    if product_id in list(cart.keys()):
        messages.info(request, "That item is already in your cart.")
        return redirect("product_detail", product_id)

    try:
        cart[product_id] = 1
        messages.success(request, f"Added {product.name} to your cart.")
        request.session["cart"] = cart
        return redirect("product_detail", product_id)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)


def remove_from_cart(request, product_id):
    """
    Remove a specified product from the cart.
    """

    try:
        cart = request.session.get("cart", {})
        product = get_object_or_404(Product, pk=product_id)
        cart.pop(product_id)
        messages.success(request, f"Removed {product.name} from your cart.")
        request.session["cart"] = cart
        return redirect("view_cart")

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
