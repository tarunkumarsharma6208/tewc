from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import *
# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=2, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, related_name='districts')
    name = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, related_name='cities')
    name = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=8, null=True)

    def __str__(self) -> str:
        return f'{self.name}'



   


class CustomUser(AbstractUser):
    # address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLES, default='customer')
    mobile = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name_plural='CustomUser'


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE, default='home')
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=8, null=True)
    address = models.TextField(null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.address}'