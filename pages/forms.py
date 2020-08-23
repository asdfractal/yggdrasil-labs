from django import forms


class ContactForm(forms.Form):
    """
    Form for user to contact business.
    """

    email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Email (required)"
        self.fields["content"].widget.attrs[
            "placeholder"
        ] = "How can we help you? (required)"
        self.fields["email"].label = False
        self.fields["content"].label = False
