from django.contrib import admin

from .models import Building, Agent, Venue, Amenity, Reservation

admin.site.register(Building)
admin.site.register(Agent)
admin.site.register(Venue)
admin.site.register(Amenity)
admin.site.register(Reservation)
