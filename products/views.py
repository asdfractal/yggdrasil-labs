from django.shortcuts import render, get_object_or_404
from reviews.models import Review
from .models import Product, Category


def products(request):
    """
    Returns a view with all products displayed.
    """
    all_products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "products": all_products,
        "categories": categories,
    }

    return render(request, "products.html", context)


def product_detail(request, product_id):
    """
    Returns a view with individual product details.
    """
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=product_id)
    context = {
        "product": product,
        "review": review,
    }

    return render(request, "product_detail.html", context)
