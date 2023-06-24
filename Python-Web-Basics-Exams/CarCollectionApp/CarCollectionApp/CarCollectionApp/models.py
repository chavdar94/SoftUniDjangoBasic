from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

MIN_AGE_VALUE = 18


def min_length_validator(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def validate_min_age(value):
    if value < MIN_AGE_VALUE:
        raise ValidationError('Age cannot be below 18')


def validate_correct_model_year(value):
    if not 1980 <= value <= 2049:
        raise ValidationError('Year must be between 1980 and 2049')


def validate_price_is_not_under_one(value):
    if value < 1:
        raise ValidationError('Price cannot be below 1')


class ProfileModel(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2

    username = models.CharField(
        null=False,
        blank=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=(min_length_validator,),
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(validate_min_age,),
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    first_name = models.CharField(
        blank=True,
        default='',
        max_length=30,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        blank=True,
        default='',
        max_length=30,
        verbose_name='Last Name',
    )
    profile_picture = models.URLField(
        blank=True,
        default='',
        verbose_name='Profile Picture',
    )


class CarModel(models.Model):
    MAX_MODEL_LENGTH = 20
    MIN_MODEL_LENGTH = 2

    CHOICES = (
        ('SPORTS CAR', 'Sports Car'),
        ('PICKUP', 'Pickup'),
        ('CROSSOVER', 'Crossover'),
        ('MINIBUS', 'Minibus'),
        ('OTHER', 'Other'),
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=CHOICES,
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_MODEL_LENGTH,
        validators=(validators.MinLengthValidator(MIN_MODEL_LENGTH),),
    )
    year = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(validate_correct_model_year,),
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(validate_price_is_not_under_one,),
    )

