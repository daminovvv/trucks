from rest_framework import serializers

from trucksapp.models import Car, Cargo, Location
from trucksapp.utils.distance_calc import calculate_distance


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarPatchSerializer(serializers.ModelSerializer):
    current_location = serializers.CharField(max_length=5, write_only=True)

    class Meta:
        model = Car
        fields = ["id", "number", "capacity", "current_location"]

    def create(self, validated_data):
        car_dict = validated_data
        car_dict["current_location"] = Location.objects.get(
            current_location=validated_data["current_location"]
        )
        car = Car.objects.create(**validated_data)
        return car


class CargoPostSerializer(serializers.ModelSerializer):
    pickup = serializers.CharField(max_length=5)
    delivery = serializers.CharField(max_length=5)

    class Meta:
        model = Cargo
        fields = ["pickup", "delivery", "weight", "description"]

    def create(self, validated_data):
        cargo_dict = validated_data
        cargo_dict["pickup"] = Location.objects.get(
            postcode=validated_data["pickup"]
        )
        cargo_dict["delivery"] = Location.objects.get(
            postcode=validated_data["delivery"]
        )
        cargo = Cargo.objects.create(**validated_data)
        return cargo


class CarChildSerializer(serializers.ModelSerializer):
    distance_miles = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ["id",
                  "number",
                  "capacity",
                  "current_location",
                  "distance_miles"]

    def get_distance_miles(self, instance):
        cargo_loc = self.context.get("cargo_loc")
        return calculate_distance(instance, cargo_loc)


class CargoSerializer(serializers.ModelSerializer):
    nearby_cars = CarChildSerializer(many=True, read_only=True)

    class Meta:
        model = Cargo
        fields = ["id", "pickup", "delivery", "weight", "nearby_cars"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        cargo_loc = instance.pickup_id
        nearby_cars = Car.objects.all().prefetch_related("current_location")
        if self.context["view"].action == "list":
            for car in nearby_cars:
                car.distance_miles = calculate_distance(car, cargo_loc)
            nearby_cars = [
                car for car in nearby_cars if car.distance_miles < 1000
            ]
        representation["nearby_cars"] = CarChildSerializer(
            nearby_cars, many=True, context={"cargo_loc": cargo_loc}
        ).data
        return representation


class CargoPatchSerializer(serializers.ModelSerializer):
    pickup_id = serializers.SerializerMethodField(read_only=True)
    delivery_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cargo
        fields = ["pickup_id", "delivery_id", "weight", "description"]

    def get_pickup_id(self, instance):
        return instance.pickup_id

    def get_delivery_id(self, instance):
        return instance.delivery_id
