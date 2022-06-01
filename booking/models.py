from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=False)
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)

    def __str__(self):
        return f'{self.user} on {self.date} from {self.start_time} to {self.end_time}'



