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
        self.prefix = "form_profile"
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


class TechSupportForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = "form_tech"
        placeholders = {
            "subject": "Subject",
            "content": "How can we help you?",
        }
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} (required)"
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False
