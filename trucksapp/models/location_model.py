from django.db import models

from trucksapp.validators import validate_postcode


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100, unique=True, validators=[validate_postcode])
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
