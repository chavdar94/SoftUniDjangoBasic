from django.db import models


class ProfileModel(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        verbose_name='Last Name',
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Link to Profile Image',
    )


class NoteModel(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Link to Image',
    )
    content = models.TextField(
        null=False,
        blank=False,
    )
