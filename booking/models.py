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

    TIMESLOT_LIST = [
            (0, '09:00 - 10:00'),
            (1, '10:00 - 11:00'),
            (2, '11:00 - 12:00'),
            (3, '12:00 - 13:00'),
            (4, '13:00 - 14:00'),
            (5, '14:00 - 15:00'),
            (6, '15:00 - 16:00'),
            (7, '16:00 - 17:00'),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_name = models.CharField(max_length=30, choices=SESSION_CHOICES, default=BEGINNER)
    date = models.DateField(auto_now_add=False, auto_now=False)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST, default=0)
    booked_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=100, default='', blank=True)

    class Meta:
        ordering = ['-booked_date']

    def time(self):
        return self.TIMESLOT_LIST[self.timeslot]
   
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

