from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "default_full_name",
            "default_phone_number",
            "default_street_address1",
            "default_street_address2",
            "default_city",
            "default_postcode",
            "default_state",
            "default_country",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_full_name": "Full name",
            "default_phone_number": "Phone number",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_city": "City",
            "default_postcode": "Postcode",
            "default_state": "State or locality",
        }
        for field in self.fields:
            if field != "default_country":
                placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False
