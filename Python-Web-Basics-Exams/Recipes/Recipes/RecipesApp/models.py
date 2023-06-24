from django.db import models


class Recipe(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    ingredients = models.CharField(
        null=False,
        blank=False,
        max_length=250
    )
    time = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Time (Minutes)'
    )

    def ingredients_list(self):
        return self.ingredients.split(', ')
