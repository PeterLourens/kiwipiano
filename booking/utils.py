import random
from django.utils import timezone
from django import forms


def date_validation(date):
    """
    To validate the booking date.
    Booking date is only available ahead of current date.
    """

    if date < timezone.now().date():
        raise forms.ValidationError('Booking can only be made ahead of today!')

