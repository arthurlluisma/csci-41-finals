from django.urls import path

from .views import landing

urlpatterns = [
    path('', landing, name='landing'),
]

app_name = "website"
