from django.db import models

from trucksapp.models.location_model import Location
from trucksapp.validators import validate_weight, validate_car_number


class Car(models.Model):
    number = models.CharField(max_length=5, unique=True, validators=[validate_car_number])
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    capacity = models.IntegerField(validators=[validate_weight])
