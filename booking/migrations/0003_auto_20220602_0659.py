# Generated by Django 3.2 on 2022-06-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20220601_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
