from django.shortcuts import render
from .models import Product


def products(request):
    """
    Returns a view with all products displayed.
    """
    products = Product.objects.all()
    context = {
        "products": products,
    }

    return render(request, "products.html", context)
