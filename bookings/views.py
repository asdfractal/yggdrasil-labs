from datetime import datetime
from django.utils.timezone import make_aware
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from checkout.models import Order
from .models import Booking
from .forms import BookingForm, BookingValidationForm


def create_booking(request, order_number):
    """
    View to create a booking if required.
    """
    order = get_object_or_404(Order, order_number=order_number)
    booking = get_object_or_404(Booking, order=order.id)
    form = BookingForm()
    if request.method == "POST":
        date_str = request.POST.get("booking_date", "")
        time_str = request.POST.get("booking_time", "")
        datetime_str = f"{date_str} {time_str}"
        try:
            datetime_obj = datetime.strptime(datetime_str, "%b %d, %Y %I:%M %p")
        except ValueError:
            messages.error(
                request, "There was a problem with your selection, please try again.",
            )
            return redirect(reverse("create_booking", args=[order_number]))

        form_validation = BookingValidationForm({"date_time": datetime_obj})
        if form_validation.is_valid():
            aware_datetime = make_aware(datetime_obj)
            booking.booking_time = aware_datetime
            booking.save()
            print("booking time updated")
            return redirect(reverse("create_booking", args=[order_number]))
        messages.error(
            request, "There was a problem with your selection, please try again."
        )
        return redirect(reverse("create_booking", args=[order_number]))

    context = {
        "booking": booking,
        "form": form,
    }
    return render(request, "bookings/create_booking.html", context)
