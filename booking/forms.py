from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Booking



class UserRegisterForm(UserCreationForm):
    """ 
    The register form is to be filled in with 
    user information for account registration.
    And automatically log user in after registration.
    """
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            auth_user = authenticate(
                username = self.cleaned_data['username'],
                password = self.cleaned_data['password1']
            )
            login(self.request, auth_user)

        return user


class UserProfileForm(forms.ModelForm):
    """
    The profile form is for user to edit user's profile information."
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
      


class ProfileUpdateForm(forms.ModelForm):
    """
    To update user profile image.
    """

    class Meta:
        model = Profile
        fields = ['profile_image', 'phone_number']




class ProfileDeleteForm(forms.ModelForm):
    """
    To delete the user profile in the database.
    """

    class Meta:
        model = User
        fields = []



class DatePicker(forms.DateInput):
    """
    To use the datepicker for the booking form.
    """
    input_type = 'date'
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])


class TimePicker(forms.TimeInput):
    """
    The time picker is to provide a range of time slot for user to choose.
    """

    input_type = 'time'



class DateTimePicker(forms.DateTimeInput):
    """
    The datetime picker is to display the booking date and time.
    """

    input_type = 'datetime'



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

class BookingForm(forms.ModelForm):
    """
    The booking form is for user to fill in
    certain informationfor booking a session.
    """
    class Meta:
        model = Booking
        exclude = ('user',)
    
        widgets = {
            'date': DatePicker(),
            'booked_date': DateTimePicker(),
            
        }

        timeslot = forms.ChoiceField(choices=TIMESLOT_LIST)


class BookingUpdateForm(forms.ModelForm):
    """
    The booking update form is for user to update the certain information for booking.
    """
    class Meta:
        model = Booking
        exclude = ('user',)
    
        widgets = {
            'date': DatePicker(),
            'start_time': TimePicker(),
            'end_time': TimePicker(),
            'booked_date': DateTimePicker(),

        }
            
