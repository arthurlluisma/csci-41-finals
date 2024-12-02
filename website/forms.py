from django import forms
from django.forms import ModelForm

from .models import Reservation

class ReservationForm(ModelForm):
    reservation_timeframe_start = forms.DateTimeField(
        label="Reservation Timeframe Start",
        widget=forms.DateTimeInput(),
    )
    reservation_timeframe_end = forms.DateTimeField(
        label="Reservation Timeframe End",
        widget=forms.DateTimeInput(),
    )

    class Meta:
        model = Reservation
        fields = [
                "reservation_participant_number",
            ]
