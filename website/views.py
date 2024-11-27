from django.shortcuts import render


# Create your views here.
def landing(request):
    ctx = {
        "tests": [
            "Test 1",
            "Test 2",
            "Test 3"
        ]
    }
    return render(request, "website/landing.html", ctx)
