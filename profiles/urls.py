from django.urls import path
from . import views


urlpatterns = [
    path("", views.profile_login_check, name="profile"),
]
