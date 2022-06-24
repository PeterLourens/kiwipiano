from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Booking


class UserRegisterForm(UserCreationForm):
    """ 
    The register form is to be filled in with 
    user information for account registration.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserProfileForm(forms.ModelForm):
    """
    The profile form is for user to edit user's profile information."
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
      


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


# class ChoiceSelector(forms.ModelForm):
#     input_type = 'session_name'


SESSION_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
        ('EXAMS_TRAINING', 'Exams Training'),
        ('LIVE_RECITAL', 'Live Recital'),
        ('VIRTUAL_PERFORMANCE', 'Virtual Performance'),
        ('REPERTOIRE_RECORDING', 'Repertoire Recording'),
        ('ONLINE_RECITAL', 'Online Recital'),
        ('END_OF_YEAR_CONCERT', 'End Of Year Concert')
    ]


class BookingForm(forms.ModelForm):
    """
    The booking form is for user to fill in certain information for booking a secssion.
    """
    class Meta:
        model = Booking
        exclude = ('user',)
    
        widgets = {
            # 'session_name': forms.ChoiceField(
            #                 widget=forms.Select(attrs={'class':'bootstrap-select'})),
            'date': DatePicker(),
            'start_time': TimePicker(),
            'end_time': TimePicker(),
            'booked_date': DateTimePicker(),
            
        }


            


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
            
