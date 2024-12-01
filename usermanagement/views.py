from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import CustomerCreationForm
from .models import Customer


def sign_up(request):
    form = CustomerCreationForm()
    customer = Customer()
    if request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            customerUser = form.save()  # creates the user
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password2"]
            user = authenticate(username=username, email=email, password=password)
            customer.user = customerUser 
            customer.customer_first_name = form.cleaned_data["first_name"]
            customer.customer_middle_initial = form.cleaned_data["middle_initial"]
            customer.customer_last_name = form.cleaned_data["last_name"]
            customer.customer_birth_date = form.cleaned_data["birth_date"]
            customer.save()
            if user is not None:
                login(request, user)
                return redirect("/website")
    ctx = {"form": form}
    return render(request, "signup.html", ctx)
