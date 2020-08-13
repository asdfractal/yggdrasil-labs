from django.shortcuts import render


def checkout(request):
    """
    Display a view to purchase items in cart.
    """
    return render(request, "checkout/checkout.html")

