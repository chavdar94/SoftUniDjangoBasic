from django.db import models


class ProfileModel(models.Model):
    NAMES_MAX_LENGTH = 30

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=NAMES_MAX_LENGTH,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=NAMES_MAX_LENGTH,
        verbose_name='Last Name',
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )


class BookModel(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=30
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    type = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
