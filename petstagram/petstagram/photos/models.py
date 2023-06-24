from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

from petstagram.pets.models import Pet
from .validators import validate_file_size

UserModel = get_user_model()


class Photo(models.Model):
    DESCRIPTION_MAX_LENGTH = 300
    LOCATION_MAX_LENGTH = 30

    photo = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        )
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
