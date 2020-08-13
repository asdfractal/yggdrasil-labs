def cart_item_count(request):
    cart = request.session.get("cart", {})
    cart_number = len(cart)
    context = {"cart_number": cart_number}

    return context
