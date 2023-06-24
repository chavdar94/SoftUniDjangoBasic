from django.db import models
from django.contrib.auth import get_user_model

from petstagram.photos.models import Photo

UserModel = get_user_model()


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 300

    comment_text = models.TextField(
        max_length=300,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
