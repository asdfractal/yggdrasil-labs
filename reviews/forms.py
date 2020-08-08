from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from products.models import Product
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        widgets = {
            "product": forms.HiddenInput(),
            "user_profile": forms.HiddenInput(),
        }
        fields = [
            "user_profile",
            "product",
            "review_content",
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_profile = user
        # product = get_object_or_404(Product, pk=product_id)
