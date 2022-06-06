from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Lesson
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages



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

    return render(request, 'account/register.html', {'form': form})


def feedback(request):
    """
    To render the registration feedback view after 
    user registered on the register view.
    """
    return render(request, 'account/register_feedback.html')


def login(request):
    """
    To render the login page.
    """

    return render(request, 'account/login.html')
   

def logout(request):
    """
    To render the logout page.
    """

    return render(request, 'account/logout.html')
   



