from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from trucksapp.models import Cargo, Car
from trucksapp.serializers import CargoSerializer, CarSerializer, CargoPostSerializer, \
    CarPatchSerializer, CarChildSerializer, CargoPatchSerializer
from trucksapp.services import load_csv, create_cars
from trucksapp.utils.distance_calc import calculate_distance


class CargoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Allows to work with cargo"""
    queryset = Cargo.objects.all()
    lookup_field = 'id'

    serializer_classes = {
        "list": CargoSerializer,
        "retrieve": CargoSerializer,
        "destroy": CargoSerializer,
        "create": CargoPostSerializer,
        "update": CargoPatchSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class CarViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Car.objects.all()
    lookup_field = 'id'
    serializer_class = CarSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return CarPatchSerializer
        return CarSerializer


def load(request):
    message = 'Служебный метод'
    # message += load_csv()
    # message += create_cars()
    return HttpResponse(message)
