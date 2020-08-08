from django.db import models
from django.contrib.auth import get_user_model

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile for storing delivery information, order history
    and other information about the clients.
    """

    curent_user = get_user_model()
    user = models.OneToOneField(curent_user, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=100, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=100, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=100, null=True, blank=True)
    default_city = models.CharField(max_length=50, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_state = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label="Country", null=True, blank=True)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
