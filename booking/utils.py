import random
from django.utils import timezone
from django.core.exceptions import ValidationError
from django import forms


def date_validation(date):
    """
    To validate the booking date.
    Booking date is only available ahead of current date.
    """

    if date < timezone.now().date():
        raise forms.ValidationError('Booking can only be made ahead of today!')



def num_validation(num):
    """
    To get valid user input for phone number.
    """

    if not num.isdigit():
        raise ValidationError('Please enter numbers only!')



def name_validation(word):
    """
    To get valid input for user names.
    """

    words = ['username', 'first_name', 'last_name']

    for word in words:

        if not word.isalpha():
            raise forms.ValidationError('Please enter only letters!')

