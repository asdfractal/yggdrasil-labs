from django import forms


class ContactForm(forms.Form):
    """
    Form for user to contact business.
    """

    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs[
            "placeholder"
        ] = "How can we help you? (required)"
        self.fields["content"].label = False
