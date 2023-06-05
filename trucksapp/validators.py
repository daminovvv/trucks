from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_weight(weight: int):
    if weight < 1 or weight > 1000:
        raise ValidationError(
            _("%(value)s is not in a range 1-1000"),
            params={"weight": weight},
        )


def validate_car_number(car_number: str):
    """number should contain 4 digits and 1 capital letter"""
    if (
        not car_number[:-1].isdigit()
        or ord(car_number[-1]) < 65
        or ord(car_number[-1]) > 90
    ):
        raise ValidationError(
            _("%(value)s should contain 4 digits and 1 capital letter"),
            params={"car_number": car_number},
        )


def validate_postcode(postcode: str):
    if not postcode.isdigit():
        raise ValidationError(
            _("%(value)s should contain digits only"),
            params={"postcode": postcode},
        )
