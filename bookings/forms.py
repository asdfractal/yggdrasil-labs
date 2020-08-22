from django import forms


class BookingForm(forms.Form):
    """
    Form to take in booking time selection.
    """

    booking_date = forms.DateField(label="Date (required)")
    booking_time = forms.TimeField(label="Time (required)")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["booking_date"].widget.attrs["class"] = "datepicker"
