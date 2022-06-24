from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Booking(models.Model):
    """
    All the lessons can only be booked once on a specific day at a specific time.
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

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    session_name = models.CharField(max_length=30, choices=SESSION_CHOICES, default=BEGINNER)
    date = models.DateField()
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)
    booked_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-booked_date']
   
    def __str__(self):
        return self.session_name


class Profile(models.Model):
    """
    Create user profile page after user login to user's account.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default_bxixmd.jpg', upload_to='profile_image')
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.user} profile'

