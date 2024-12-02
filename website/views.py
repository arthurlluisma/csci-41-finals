from django.shortcuts import render, redirect

from usermanagement.models import Customer

from .forms import ReservationForm
from .models import Agent, Amenity, Building, Reservation, Venue


# Create your views here.
def landing(request):
    # logged in
    if request.user.is_authenticated:
        # return user details
        customer = Customer.objects.get(user=request.user)
        customer_info = {
            "first_name": customer.customer_first_name,
            "middle_initial": customer.customer_middle_initial,
            "last_name": customer.customer_last_name,
            "birth_date": customer.customer_birth_date,
            "location": customer.customer_location,
        }
        customer_reservations = Reservation.objects.filter(customer=customer)
        # check for remove reservation
        if request.method == "POST":
            reservation_to_remove = request.POST.get("reservation")
            reservation_to_remove = Reservation.objects.get(pk=reservation_to_remove)
            reservation_to_remove.delete()
    # logged out
    else:
        customer_info = {}
        customer_reservations = {}
    # available venues
    search_query = request.GET.get("search")
    building_query = request.GET.get("building")
    type_query = request.GET.get("type")
    available_venues = Venue.objects.filter(
        renovation_status__icontains="no",
    )
    if search_query != "" and search_query is not None:
        available_venues = available_venues.filter(venue_name__icontains=search_query)
    if building_query != "" and building_query is not None:
        available_venues = available_venues.filter(
            building__building_name__icontains=building_query
        )
    if type_query != "" and type_query is not None:
        available_venues = available_venues.filter(venue_type__icontains=type_query)
    # available buildings
    available_building_nums = (
        Venue.objects.filter(
            renovation_status__icontains="no",
        )
        .values("building")
        .distinct()
    )
    available_buildings = []
    for building in available_building_nums:
        available_buildings += Building.objects.filter(building_id=building["building"])
    # available venue types
    available_venue_types = (
        Venue.objects.filter(
            renovation_status__icontains="no",
        )
        .values("venue_type")
        .distinct()
    )

    venue_info = {
        "venue_buildings": available_buildings,
        "venue_types": available_venue_types,
    }
    ctx = {
        "customer": customer_info,
        "customer_reservations": customer_reservations,
        "venues": available_venues,
        "venue_info": venue_info,
    }
    return render(request, "website/landing.html", ctx)


def venue(request, pk):
    venue = Venue.objects.get(pk=pk)
    amenities = Amenity.objects.filter(venue=venue)
    # logged in
    if request.user.is_authenticated:
        # return user details
        customer = Customer.objects.get(user=request.user)
        customer_info = {
            "first_name": customer.customer_first_name,
            "middle_initial": customer.customer_middle_initial,
            "last_name": customer.customer_last_name,
            "birth_date": customer.customer_birth_date,
        }
        new_reservation = Reservation()
        if request.method == "POST":
            form = ReservationForm(request.POST)
            if form.is_valid():
                new_reservation.reservation_participant_number = form.cleaned_data.get(
                    "reservation_participant_number"
                )
                new_reservation.reservation_timeframe_start = form.cleaned_data.get(
                    "reservation_timeframe_start"
                )
                new_reservation.reservation_timeframe_end = form.cleaned_data.get(
                    "reservation_timeframe_end"
                )
                new_reservation.venue = venue
                new_reservation.customer = Customer.objects.get(user=request.user)
                new_reservation.save()
                return redirect("/")
    # logged out
    else:
        customer_info = {}
    form = ReservationForm()
    ctx = {
        "customer": customer_info,
        "venue": venue,
        "amenities": amenities,
        "form": form,
    }
    return render(request, "website/venue.html", ctx)
