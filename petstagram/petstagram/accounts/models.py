from enum import Enum

from django.db import models
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator


def validate_isalpha(value):
    return value.isalpha()


class AppUser(auth_models.AbstractUser):
    class Gender(models.TextChoices):
        male = 'Male', 'Male'
        female = 'Female', 'Female'
        DoNotShow = 'Do Not Show', 'Do not show'

        @classmethod
        def max_len(cls):
            return max(len(value) for _, value in cls.choices)

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(2), validate_isalpha),
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(2), validate_isalpha),
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        choices=Gender.choices,
        max_length=Gender.max_len(),
        null=True,
        blank=True,
        default=Gender.DoNotShow
    )

    def get_user_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username
