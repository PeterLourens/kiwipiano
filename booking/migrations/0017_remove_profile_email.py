# Generated by Django 3.2 on 2022-06-18 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]