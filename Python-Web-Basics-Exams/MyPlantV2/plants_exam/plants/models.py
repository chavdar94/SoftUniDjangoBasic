from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from enum import Enum

from django.urls import reverse_lazy

from .validators import check_name_capital_letter, plant_name_only_letters, plant_price_validator, PlantPriceValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)]
    )
    first_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[check_name_capital_letter]
    )
    last_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[check_name_capital_letter]
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(c.value, c.value) for c in cls]

    @classmethod
    def max_length(cls):
        return max(len(c.value) for c in cls)


class PlantChoices(ChoicesEnum):
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'


class Plant(models.Model):
    # CHOICES = (
    #     ('Outdoor Plants', 'Outdoor Plants'),
    #     ('Indoor Plants', 'Indoor Plants')
    # )

    plant_type = models.CharField(
        max_length=PlantChoices.max_length(),
        null=False,
        blank=False,
        choices=PlantChoices.choices(),
    )
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), plant_name_only_letters]
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[PlantPriceValidator('Price can not be negative (from class)')]
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
