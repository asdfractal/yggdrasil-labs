from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order, OrderLineItem
from .models import Booking
from .forms import BookingForm


@login_required
def create_booking(request, order_number):
    """
    View to create a booking if required.
    """
    order = get_object_or_404(Order, order_number=order_number)
    booking = get_object_or_404(Booking, order=order.id)
    lineitems = OrderLineItem.objects.filter(order=order.id)
    form = BookingForm()
    booking_item = None
    for item in lineitems:
        if item.product.booking_required:
            booking_item = item.product.name
            break

    if request.method == "POST":
        date_str = request.POST.get("booking_date", "")
        time_str = request.POST.get("booking_time", "")
        try:
            date_obj = datetime.strptime(date_str, "%d %b, %Y").date()
            time_obj = datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            messages.error(
                request, "There was a problem with your selection, please try again.",
            )
            return redirect(reverse("create_booking", args=[order_number]))
        form_data = {
            "booking_date": date_obj,
            "booking_time": time_obj,
        }
        form = BookingForm(form_data)
        if form.is_valid():
            booking.booking_date = date_obj
            booking.booking_time = time_obj
            booking.save()
            messages.success(
                request, f"Booking created at {time_str} on {date_str}.",
            )
            return redirect(reverse("profile"))
        messages.error(
            request, "There was a problem with your selection, please try again."
        )
        return redirect(reverse("create_booking", args=[order_number]))

    context = {
        "booking": booking,
        "booking_item": booking_item,
        "form": form,
        "page_title": "Booking",
    }
    return render(request, "bookings/create_booking.html", context)
