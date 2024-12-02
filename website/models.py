from django.db import models
from django.urls import reverse

from usermanagement.models import Customer


class Building(models.Model):
    building_id = models.BigAutoField(primary_key=True)  # primary key
    building_name = models.CharField(max_length=255, default="Wellrock Tower")
    street_num = models.CharField(max_length=255, default="1st Street")
    district_num = models.CharField(max_length=255, default="1st District")
    city_name = models.CharField(max_length=255, default="Quezon City")

    def __str__(self):
        return self.building_name


class Agent(models.Model):
    agent_id = models.CharField(max_length=255, primary_key=True)  # primary key
    agent_first_name = models.CharField(max_length=255)
    agent_last_name = models.CharField(max_length=255)
    manager = models.ForeignKey(
        "self", on_delete=models.RESTRICT, blank=True, null=True
    )
    building = models.ForeignKey(Building, on_delete=models.RESTRICT)

    def __str__(self):
        return "{} {}".format(self.agent_first_name, self.agent_last_name)


class Venue(models.Model):
    venue_id = models.BigAutoField(primary_key=True)  # primary key
    venue_name = models.CharField(max_length=255, default="General Room")
    venue_type = models.CharField(max_length=255, default="Function Hall")
    venue_floor_num = models.CharField(max_length=2, default="GF")
    venue_floor_area = models.CharField(max_length=255, default="20 sqm")
    venue_capacity = models.CharField(max_length=255, default="20 max")
    renovation_status = models.CharField(max_length=5, default="No")
    agent = models.ForeignKey(Agent, on_delete=models.RESTRICT)
    building = models.ForeignKey(Building, on_delete=models.RESTRICT)

    def __str__(self):
        return self.venue_name

    def get_absolute_url(self):
        return reverse("website:venue", args=[self.pk])


class Amenity(models.Model):
    amenity_id = models.CharField(max_length=255, primary_key=True)  # primary key
    amenity_type = models.CharField(max_length=255, default="Chair")
    amenity_category = models.CharField(max_length=255, default="Furniture")
    amenity_description = models.CharField(
        max_length=255, default="A piece of furniture equipment"
    )
    amenity_quantity = models.CharField(max_length=255, default="1pc.")
    venue = models.ForeignKey(Venue, on_delete=models.RESTRICT)

    def __str__(self):
        return self.amenity_type


class Reservation(models.Model):
    reservation_id = models.BigAutoField(primary_key=True)  # primary key
    reservation_participant_number = models.CharField(max_length=255, default="0 pax")
    reservation_timeframe_start = models.DateTimeField(
        auto_now=False, auto_now_add=False
    )
    reservation_timeframe_end = models.DateTimeField(
        auto_now=False, auto_now_add=False
    )
    venue = models.ForeignKey(Venue, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
