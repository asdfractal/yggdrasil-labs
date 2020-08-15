from django.shortcuts import render, get_object_or_404

from .models import Booking


def create_booking(request):
    """
    View to create a booking if required.
    """
    # booking = get_object_or_404(Booking, order=order_number)

    return render(request, "bookings/create_booking.html")

