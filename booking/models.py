from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Booking(models.Model):

    """
    All the lessons can only be booked once on a specific day at a specific time.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    lesson_name = models.CharField(max_length=30, blank=True)
    date = models.DateField()
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)
    booked_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=True)


    class Meta:
        ordering = ['-booked_date']
   

    def __str__(self):
        return f'{self.user} on {self.date} at {self.start_time}'




STATUS = ((0, "Available"), (1, "Unavailable"))
class Lesson(models.Model):
    """
    There are 4 different lessons.
    """

    LessonType = (('Beginner', 'Beginner'), ('Intermedia', 'Intermedium'), ('Advanced', 'Advanced'), ('Examination-training', 'Examination-training'))
    
 
    lesson_name = models.CharField(max_length=30, choices=LessonType)
    lesson_date = models.DateField(blank=False)
    start_time = models.TimeField(auto_now_add=False)
    lesson_status = models.IntegerField(choices=STATUS, default=0)


    def __str__(self):
        return f'Lesson {self.lesson_name} is {self.lesson_status} on {self.lesson_date} at {self.start_time}'




class Profile(models.Model):
    """
    Create user profile page after user login to user's account.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #date_of_birth = models.DateField()
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_image')
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        # return f'{self.first_name} Profile'
        return self.user.username

