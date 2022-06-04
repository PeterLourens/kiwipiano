from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(forms.ModelForm):
    """ 
    The register form is to be filled in with 
    user information for account registration.
    """

   
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

