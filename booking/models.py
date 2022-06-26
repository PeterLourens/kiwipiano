from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from datetime import datetime, date
from booking.utils import date_validation, num_validation, name_validation


class Booking(models.Model):
    """
    To create a booking where user can book a session.
    """
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    EXAMS_TRAINING = 'Exams Training'
    LIVE_RECITAL = 'Live Recital'
    VIRTUAL_PERFORMANCE = 'Virtual Performance'
    REPERTOIRE_RECORDING = 'Repertoire Recording'
    ONLINE_RECITAL = 'Online Recital'
    END_OF_YEAR_CONCERT = 'End Of Year Concert'
    
    SESSION_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (EXAMS_TRAINING, 'Exams Training'),
        (LIVE_RECITAL, 'Live Recital'),
        (VIRTUAL_PERFORMANCE, 'Virtual Performance'),
        (REPERTOIRE_RECORDING, 'Repertoire Recording'),
        (ONLINE_RECITAL, 'Online Recital'),
        (END_OF_YEAR_CONCERT, 'End Of Year Concert')
    ]

    TIMESLOT_CHOICES = [
        ('09:00 - 10:00', '09:00 - 10:00'),
        ('10:00 - 11:00', '10:00 - 11:00'),
        ('11:00 - 12:00', '11:00 - 12:00'),
        ('12:00 - 13:00', '12:00 - 13:00'),
        ('13:00 - 14:00', '13:00 - 14:00'),
        ('14:00 - 15:00', '14:00 - 15:00'),
        ('15:00 - 16:00', '15:00 - 16:00'),
        ('16:00 - 17:00', '16:00 - 17:00'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, validators=[name_validation])
    session_name = models.CharField(max_length=30, choices=SESSION_CHOICES, default=BEGINNER)
    date = models.DateField(auto_now_add=False, auto_now=False, validators=[date_validation])
    timeslot = models.CharField(max_length=200, choices=TIMESLOT_CHOICES, default='09:00 - 10:00')
    booked_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=100, default='', blank=True)

    class Meta:
        ordering = ['-booked_date']

    def timelot(self):
        return self.TIMESLOT_CHOICES[self.timeslot]
   
    def __str__(self):
        return self.session_name


class Profile(models.Model):
    """
    Create user profile page after user register and login to user's account.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, validators=[name_validation])
    profile_image = models.ImageField(default='default_bxixmd.jpg', upload_to='profile_image')
    phone_number = models.CharField(max_length=50, null=True, blank=True, validators=[num_validation])
    password = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return f'{self.user} profile'

