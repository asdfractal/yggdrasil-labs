from tastypie.resources import ModelResource, ALL

from bookings.models import Booking


class BookingResource(ModelResource):
    """
    Queries the Booking model and filters by date.
    """

    class Meta:
        queryset = Booking.objects.all()
        resource_name = "booking"
        filtering = {
            "booking_date": ALL,
        }
