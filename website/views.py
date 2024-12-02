from django.shortcuts import render

from usermanagement.models import Customer
from .models import Building, Agent, Venue, Amenity, Reservation

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
            "birth_date": customer.customer_birth_date
        }
        customer_reservations = Reservation.objects.filter(customer=customer)
    # logged out
    else:
        customer_info = {}
        customer_reservations = {}
    venues = Venue.objects.filter(renovation_status__icontains="no")
    ctx = {
        "customer": customer_info,
        "customer_reservations": customer_reservations,
        "venues": venues
    }
    return render(request, "website/landing.html", ctx)

def reservations(request):
    ctx = {
        "tests": [
            "Test 1",
            "Test 2",
            "Test 3"
        ]
    }
    return render(request, "website/reservations.html", ctx)
