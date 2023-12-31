# Generated by Django 4.2 on 2023-04-11 13:38

import GamesPlayApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesPlayApp', '0002_alter_gamemodel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='max_level',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[GamesPlayApp.models.validate_max_level], verbose_name='Max Level'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
