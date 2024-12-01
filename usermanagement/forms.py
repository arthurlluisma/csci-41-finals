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

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         self.cleaned_data["username"],
    #         self.cleaned_data["email"],
    #         self.cleaned_data["password1"],
    #     )
    #     customer = Customer(
    #         user=user,
    #         customer_first_name=self.cleaned_data["first_name"],
    #         customer_middle_initial=self.cleaned_data["middle_inital"],
    #         customer_last_name=self.cleaned_data["last_name"],
    #         customer_birth_date=self.cleaned_data["birth_date"],
    #     )
    #     customer.save()
    #     return customer
