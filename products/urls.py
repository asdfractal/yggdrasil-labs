from django.urls import path
from . import views


urlpatterns = [
    path("", views.products, name="products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("<int:product_id>/reviews/", views.product_reviews, name="product_reviews"),
    path("<int:product_id>/reviews/delete/", views.delete_review, name="delete_review"),
]
