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
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password1']
            )
            login(self.request, auth_user)

        return user


class UserProfileForm(forms.ModelForm):
    """
    The profile form is for user to edit user's profile information."
    """
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'profile_image',
            'first_name_profile',
            'last_name_profile'
        ]


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


class DateTimePicker(forms.DateTimeInput):
    """
    The datetime picker is to display the booking date and time.
    """
    input_type = 'datetime'


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


class BookingUpdateForm(forms.ModelForm):
    """
    The booking update form is for user to update
    the certain information for booking.
    """
    class Meta:
        model = Booking
        exclude = ('user',)
        widgets = {
            'date': DatePicker(),
            'booked_date': DateTimePicker(),
        }
