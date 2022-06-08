from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Lesson
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegisterForm
#from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def home(request):
    """
    To render the home view.
    """
   
    return render(request, 'index.html')

# class Home(View):

#     def get(self, request):
#         return render(request, 'index.html')




def register(request):
    """
    To render the register view.
    """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account registration is successful!')


            return redirect('feedback')
            
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def feedback(request):
    """
    To render the registration feedback view after 
    user registered on the register view.
    """
    return render(request, 'accounts/register_feedback.html')


def login_view(request):
    """
    To render the login page to log user in the account.
    """

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request, user)

            return redirect('profile')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})



@login_required
def profile(request):
    """
    To render the user profile page.
    """

    context = {
        'user': request.user
    }

   
    return render(request, 'accounts/profile.html', context)
   


def logout_view(request):
    """
    To render the logout page.
    """

    logout(request)

    return render(request, 'accounts/logout.html')



