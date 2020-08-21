from django import forms


class BookingForm(forms.Form):
    """
    Form to take in booking time selection.
    """

    booking_date = forms.CharField(label="Date (required)")
    booking_time = forms.CharField(label="Time (required)")

    def __init__(self, *args, **kwargs):
        """
        Customize form display.
        """
        super().__init__(*args, **kwargs)
        self.fields["booking_date"].widget.attrs["class"] = "datepicker"
        self.fields["booking_time"].widget.attrs["class"] = "timepicker"


class BookingValidationForm(forms.Form):
    """
    Form to validate selection is correct format.
    """

    date_time = forms.DateTimeField()
