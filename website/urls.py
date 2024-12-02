from django.urls import path

from .views import landing, venue

urlpatterns = [
    path('', landing, name='landing'),
    path('venue/<int:pk>', venue, name='venue'),
]

app_name = "website"
