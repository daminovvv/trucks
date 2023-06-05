from rest_framework import mixins, viewsets

from trucksapp.models import Car, Cargo
from trucksapp.serializers import (CargoPatchSerializer, CargoPostSerializer,
                                   CargoSerializer, CarPatchSerializer,
                                   CarSerializer)


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
    lookup_field = "id"

    serializer_classes = {
        "list": CargoSerializer,
        "retrieve": CargoSerializer,
        "destroy": CargoSerializer,
        "create": CargoPostSerializer,
        "update": CargoPatchSerializer,
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
    lookup_field = "id"
    serializer_class = CarSerializer

    def get_serializer_class(self):
        if self.action == "update":
            return CarPatchSerializer
        return CarSerializer
