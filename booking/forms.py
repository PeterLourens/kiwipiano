from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """ 
    The register form is to be filled in with 
    user information for account registration.
    """

   
    email = forms.EmailField()
    #password = forms.PasswordInput()
   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserProfileForm(forms.ModelForm):
    """
    The profile form is for user to edit user's profile information."
    """

    class Meta:
        model = Profile
        fields = ('user', 'profile_image', 'first_name', 'last_name', 'email_address', 'phone_number', 'password')
        labels = {
            'user': 'Username',
            'profile_image': 'Profile_image',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email',
            'phone_number': 'Phone Number',
            'password': 'Password'
        }
   
