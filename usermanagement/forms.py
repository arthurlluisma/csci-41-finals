from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomerCreationForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=255)
    middle_initial = forms.CharField(label="Middle Initial", max_length=255)
    last_name = forms.CharField(label="Last Name", max_length=255)
    birth_date = forms.DateField(
        label="Birth Date",
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
