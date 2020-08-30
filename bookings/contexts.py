import datetime
from django.contrib import messages
from django.utils.safestring import mark_safe

from profiles.models import UserProfile
from .models import Booking


def check_booking_status(request):
    """
    Checks if the user has a booking that needs to be set and notifies them via
    messages. Sets a cookie with a 10 minute expiry and checks this before sending
    message and setting it again.
    """
    user_profile = None
    bookings = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        bookings = Booking.objects.filter(user_profile=user_profile)
    expire_at = datetime.datetime.now() + datetime.timedelta(minutes=10)
    notification_expired = True
    check_session = request.session.get("booking_notification", {})
    if check_session.get("expire_at", 0) > datetime.datetime.now().timestamp():
        notification_expired = False

    if bookings:
        if notification_expired:
            if check_session:
                del request.session["booking_notification"]
            for booking in bookings:
                if not booking.booking_time:
                    messages.info(
                        request,
                        mark_safe(
                            "You have an available booking to create. Please visit your \
                             <a href='/profile/#bookings'>bookings page</a> to confirm."
                        ),
                    )
                    request.session["booking_notification"] = {
                        "value": True,
                        "expire_at": expire_at.timestamp(),
                    }
                    break

    context = {
        "bookings": bookings,
    }
    return context
