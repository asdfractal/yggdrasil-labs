from random import randint
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from reviews.models import Review
from reviews.forms import ReviewForm
from profiles.models import UserProfile
from checkout.models import Order
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
        "page_title": "Products",
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """
    Returns a view with individual product details and a random review to display.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    review = ""
    if len(reviews) > 0:
        pks = reviews.values_list("pk", flat=True)
        random = randint(0, len(pks) - 1)
        review = Review.objects.get(pk=pks[random])
    context = {
        "product": product,
        "review": review,
        "page_title": product.name,
    }

    return render(request, "products/product-detail.html", context)


def product_reviews(request, product_id):
    """
    Returns a view with all the reviews for a specific product. If current user
    has a review, get that and allow them to update.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    user_orders = Order.objects.filter(user_profile=user_profile)
    form = ReviewForm
    user_review = ""
    user_purchased = False
    for review in reviews:
        if review.user_profile == user_profile:
            user_review = review
            form = ReviewForm(instance=user_review)

    for order in user_orders:
        for item in order.lineitems.all():
            if item.product == product:
                user_purchased = True

    if request.method == "POST":
        if user_review != "":
            form = ReviewForm(request.POST, instance=user_review)
        else:
            if len(request.POST["review_content"]) <= 15:
                messages.error(
                    request,
                    "Review not long enough, please write a review longer than 15 characters.",
                )
                return redirect(reverse("product_reviews", args=(product_id,)))
            form_data = {
                "review_content": request.POST["review_content"],
            }
            form = ReviewForm(form_data)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_profile = user_profile
            review.product = product
            review.save()
            messages.success(request, "Review added.")
            return redirect(reverse("product_reviews", args=(product_id,)))

        messages.error(request, "Error adding review.")
        return redirect(reverse("product_reviews", args=(product_id,)))

    context = {
        "product": product,
        "reviews": reviews,
        "form": form,
        "user_review": user_review,
        "user_purchased": user_purchased,
        "page_title": f"{product.name} reviews",
    }

    return render(request, "products/product-reviews.html", context)


def delete_review(request, product_id):
    """
    Give user ability to delete their review.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    review = get_object_or_404(Review, user_profile=user_profile, product=product_id)
    review.delete()
    messages.info(request, "Review deleted.")
    return redirect(reverse("product_reviews", args=(product_id,)))
