from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
import re


def validate_user_name(value):
    pattern = r'\w+$'
    match = re.match(pattern, value)
    if not match:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2
    AGE_MIN_VALUE = 0

    username = models.CharField(
        null=False,
        blank=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_user_name
        ),
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[validators.MinValueValidator(AGE_MIN_VALUE)]
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    GENRE_CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other')
    )

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=ALBUM_NAME_MAX_LENGTH,
        verbose_name='Album Name',
    )
    artist = models.CharField(
        null=False,
        blank=False,
        max_length=ARTIST_NAME_MAX_LENGTH
    )
    genre = models.CharField(
        null=False,
        blank=False,
        max_length=GENRE_MAX_LENGTH,
        choices=GENRE_CHOICES,

    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(0.0, 'The price cannot be below 0.0')]
    )
