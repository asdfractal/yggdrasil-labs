from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def products(request):
    """
    Returns a view with all products displayed.
    """
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "products.html", context)

def product_detail(request, product_id):
    """
    Returns a view with individual product details.
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }

    return render(request, 'product_detail.html', context)
