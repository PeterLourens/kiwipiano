# Generated by Django 3.2 on 2022-06-25 08:28

import booking.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0027_auto_20220624_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(validators=[booking.utils.date_validation]),
        ),
    ]