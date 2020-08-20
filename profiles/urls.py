from django.urls import path
from . import views


urlpatterns = [
    path("", views.profile_login_check, name="profile"),
    path("order/<order_number>/", views.order_details, name="order_details"),
]
