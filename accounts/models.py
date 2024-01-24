from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import *
# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=2, null=True)

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, related_name='districts')
    name = models.CharField(max_length=100, null=True)

class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, related_name='cities')
    name = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=8, null=True)

class Address(models.Model):
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE, default='home')
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    destrict = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=8, null=True)
    address = models.TextField(null=True)


class CustomUser(AbstractUser):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    destrict = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    dob = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLES, default='customer')
