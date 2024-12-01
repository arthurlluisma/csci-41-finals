from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.BigAutoField(primary_key=True) # primary key
    customer_first_name = models.CharField(max_length=255)
    customer_middle_initial = models.CharField(max_length=255)
    customer_last_name = models.CharField(max_length=255)
    customer_birth_date = models.DateField(auto_now=False, auto_now_add=False)
