from django.urls import path
from . import views


urlpatterns = [
    path("<order_number>/", views.create_booking, name="create_booking"),
]
