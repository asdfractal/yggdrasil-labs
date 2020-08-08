from django.urls import path
from . import views


urlpatterns = [
    path("<profile_id>/", views.profile, name="profile"),
]
