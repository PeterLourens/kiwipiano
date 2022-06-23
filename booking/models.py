from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime



STATUS = [(0, 'Available'), (1, 'Unavailable')]




class Booking(models.Model):

    """
    All the lessons can only be booked once on a specific day at a specific time.
    """
    
    SESSION_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Exams-training', 'Exams-training'),
        ('Live-recital', 'Live-recital'),
        ('Virtual-performance', 'Virtual-performance'),
        ('Repertoire-recording', 'Repertoire-recording'),
        ('Online-recital', 'Online-recital'),
        ('End-of-year-concert', 'End-of-year-concert')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    session_name = models.CharField(max_length=30, choices=SESSION_CHOICES, default='Beginner')
    date = models.DateField()
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)
    booked_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=True)


    class Meta:
        ordering = ['-booked_date']
   

    def __str__(self):
        return f'{self.session_name} on {self.date} at {self.start_time}'




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



