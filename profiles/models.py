import uuid
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
    personal_key = models.CharField(max_length=32, null=True, blank=True)

    @staticmethod
    def _generate_personal_key():
        """
        Generate an personal key using UUID.
        """
        return uuid.uuid4().hex.upper()

    def check_personal_key(self):
        """
        Generate a key if client and key doesn't exist.
        """
        if self.is_client:
            if not self.personal_key:
                self.personal_key = self._generate_personal_key()
                self.save()

    def __str__(self):
        return self.user.username
