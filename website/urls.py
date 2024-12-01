from django.urls import path

from .views import landing, reservations

urlpatterns = [
    path('', landing, name='landing'),
    path('reservations', reservations, name='landing'),
]

app_name = "website"
