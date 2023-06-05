from django.db import models

from trucksapp.models.location_model import Location
from trucksapp.validators import validate_weight


class Cargo(models.Model):
    pickup = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="pickup_cargo"
    )
    delivery = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="delivery_cargo"
    )
    weight = models.IntegerField(validators=[validate_weight])
    description = models.TextField()
