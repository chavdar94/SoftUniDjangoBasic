# Generated by Django 4.2.1 on 2023-05-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_appuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do Not Show', 'Do not show')], default='Do Not Show', max_length=11, null=True),
        ),
    ]
