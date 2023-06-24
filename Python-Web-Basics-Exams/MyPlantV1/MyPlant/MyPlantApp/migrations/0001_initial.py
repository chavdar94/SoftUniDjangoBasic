# Generated by Django 4.2 on 2023-04-10 14:32

import MyPlantApp.validators.profile_validators.profile_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('OUTDOOR PLANTS', 'Outdoor Plants'), ('INDOOR PLANTS', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), MyPlantApp.validators.profile_validators.profile_validators.check_string_only_letters])),
                ('image_url', models.CharField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[MyPlantApp.validators.profile_validators.profile_validators.check_for_capital_first_letter])),
                ('last_name', models.CharField(max_length=20, validators=[MyPlantApp.validators.profile_validators.profile_validators.check_for_capital_first_letter])),
                ('profile_picture', models.CharField(blank=True, null=True)),
            ],
        ),
    ]
