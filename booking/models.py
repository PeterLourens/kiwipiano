from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #email = models.EmailField()
    lesson_name = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=False)
    #time = models.CharField(max_length=30)
    start_time = models.TimeField(auto_now_add=False)
    #end_time = models.TimeField(auto_now_add=False)
    #booked_date = models.DateTimeField(default=timezone.now)
    booked_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=True)
   

    def __str__(self):
        return f'{self.user} on {self.date} at {self.time}'


