from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["review_content"]
        widgets = {
            "review_content": forms.Textarea(
                attrs={"disabled": True, "class": "review-form-textarea", "rows": 5,}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["review_content"].label = "Write your review"