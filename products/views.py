from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from reviews.models import Review
from reviews.forms import ReviewForm
from profiles.models import UserProfile
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
    reviews = Review.objects.filter(product=product_id)
    context = {
        "product": product,
        "reviews": reviews,
    }

    return render(request, "product-detail.html", context)


def product_reviews(request, product_id):
    """
    Returns a view with all the reviews for a specific product.
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    print(user)
    print(user.id)
    form = ReviewForm(user)
    if request.method == "POST":
        form_data = {
            "user_profle": user,
            "product": product,
            "review_content": request.POST["review_content"],
        }
        form = ReviewForm(user, form_data)
        print(form_data)
        if form.is_valid():
            review = form.save(product_id)
            review.save()

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)

    context = {
        "product": product,
        "reviews": reviews,
        "form": form,
    }

    return render(request, "product-reviews.html", context)
