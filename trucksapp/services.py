import csv
import random

from trucksapp.models import Location, Car


def load_csv():
    with open('./uszips.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        count = 0
        for row in reader:
            b = {
                'city': row['city'],
                'state': row['state_name'],
                'postcode': row['zip'],
                'latitude': row['lat'],
                'longitude': row['lng'],
            }
            a = Location(**b)
            a.save()
            count += 1
        return f'\nСоздано {count} локаций'


def create_cars():
    number = '1000'
    for i in range(20):
        car = Car(**{
            'number': chr(65 + i) + number,
            'current_location': Location.objects.get(pk=random.randint(1, 33789)),
            'capacity': random.randint(1, 1000),
        })
        car.save()
    return '\nСоздано 20 машин'
