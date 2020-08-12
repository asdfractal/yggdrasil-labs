from django.shortcuts import render


def cart(request):
    """
    Display users shopping cart.
    """

    return render(request, "cart/cart.html")
