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
   

    def __str__(self):
        return f'{self.user} on {self.date} at {self.start_time}'



