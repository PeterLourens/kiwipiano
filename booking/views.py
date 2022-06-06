from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Lesson
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login



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
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account registration is successful!')

            login(request, user)

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

    if request.method == 'GET':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request, user)

            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
   

def logout_view(request):
    """
    To render the logout page.
    """

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            logout(request, user)

            return redirect('login')

    return render(request, 'accounts/logout.html')
   



