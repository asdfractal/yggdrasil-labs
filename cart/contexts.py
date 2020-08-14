from django.shortcuts import get_object_or_404
from products.models import Product


def get_cart_items(request):
    cart_items = []
    cart_total = 0
    cart = request.session.get("cart", {})
    cart_number = len(cart)

    for key in list(cart.keys()):
        product = get_object_or_404(Product, pk=key)
        product_price = product.price
        cart_total += product_price
        cart_items.append(
            {"product": product,}
        )

    context = {
        "cart_items": cart_items,
        "cart_total": cart_total,
        "cart_number": cart_number,
    }

    return context
