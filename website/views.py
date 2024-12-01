from django.shortcuts import render

from usermanagement.models import Customer

# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        # return user details
        customer = Customer.objects.get(user=request.user)
        customerInfo = {
            "first_name": customer.customer_first_name,
            "middle_initial": customer.customer_middle_initial,
            "last_name": customer.customer_last_name,
            "birth_date": customer.customer_birth_date
        }
    else:
        customerInfo = {}
    ctx = {
        "customer": customerInfo,
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
