from django.core import validators
from django.db import models

from MyPlantApp.validators.profile_validators.profile_validators import check_for_capital_first_letter, \
    check_string_only_letters


class ProfileModel(models.Model):
    PROFILE_MAX_LENGTH = 10
    PROFILE_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 20

    username = models.CharField(
        blank=False,
        null=False,
        max_length=PROFILE_MAX_LENGTH,
        validators=(validators.MinLengthValidator(PROFILE_MIN_LENGTH),)
    )
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=NAME_MAX_LENGTH,
        validators=(check_for_capital_first_letter,),
        verbose_name='First Name'
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=NAME_MAX_LENGTH,
        validators=(check_for_capital_first_letter,),
        verbose_name='Last Name'
    )
    profile_picture = models.URLField(
        null=True,
        blank=True
    )


class PlantModel(models.Model):
    TYPE_MAX_LENGTH = 14
    PLANT_NAME_MAX_LENGTH = 20
    PLANT_NAME_MIN_LENGTH = 2

    CHOICES = (
        ('OUTDOOR PLANTS', 'Outdoor Plants'),
        ('INDOOR PLANTS', 'Indoor Plants')
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=TYPE_MAX_LENGTH,
        choices=CHOICES
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=PLANT_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(PLANT_NAME_MIN_LENGTH),
            check_string_only_letters
        )
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False
    )
