from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def check_name_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def plant_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')


def plant_price_validator(value):
    if value <= 0:
        raise ValidationError('Price can not be negative!')


@deconstructible
class PlantPriceValidator:
    def __init__(self, message=None):
        self.min_price = 0
        if message:
            self.message = message

    def __call__(self, value):
        if value <= self.min_price:
            raise ValidationError(self.message)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.min_price == other.min_price
