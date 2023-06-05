from decimal import Decimal

from geopy.distance import geodesic

from trucksapp.models import Location


def calculate_distance(car_instance, cargo_loc):
    cargo_loc = Location.objects.get(pk=cargo_loc)
    point_a = (cargo_loc.latitude, cargo_loc.longitude)

    car_loc = car_instance.current_location
    point_b = (car_loc.latitude, car_loc.longitude)
    distance_miles = Decimal(geodesic(point_a, point_b).miles)\
        .quantize(Decimal("1.00"))

    return distance_miles
