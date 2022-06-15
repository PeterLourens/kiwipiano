from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Profile, Booking
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import (
    UserRegisterForm, 
    UserProfileForm, 
    ProfileUpdateForm, 
    BookingForm
)

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def home(request):
    """
    To render the home view.
    """
   
    return render(request, 'index.html')



def sign_up(request):
    """
    To render the register page.
    The form is to be filled in with user information for account registration.
    """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Welcome { username}! Your account has been created!')

            return redirect('feedback')

    else:
        form = UserRegisterForm()

   
    return render(request, 'account/signup.html', {'form': form})



def login(request):

    """
    To render the login page for logging user into the account.
    """

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request)

            return redirect('home')

    else:
        form = AuthenticationForm()


    return render(request, 'account/login.html')



def logout_view(request):
    """
    To render the home page after user logged out the account.
    """

    logout(request)

    return render(request, 'index.html')




def feedback(request):
    """
    To render the registration feedback view after 
    user registered on the register view.
    """
    return render(request, 'account/register_feedback.html')



@login_required
def profile(request):
    """
    To render the user profile page with user's personal information.
    """
   
    return render(request, 'profile/profile.html')
   


def update_profile(request):
    """
    To render the update profile page.
    """

    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_profile_form.is_valid() and profile_update_form.is_valid():
            user_profile_form.save()
            profile_update_form.save()

            messages.success(request, f'Your profile has been updated.')

            return redirect('profile')

        else:
            messages.error(request, f'Please try again.')

    else:
        user_profile_form = UserProfileForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

   
    context = {
    
        'user_profile_form': user_profile_form,
        'profile_update_form': profile_update_form,
      
    }
   
    return render(request, 'profile/update_profile.html', context)




def booking_login(request):
    """
    To render the booking login alert page. When user clicks the booking btn,
    it asks user to login or register an account first.
    """


    return render(request, 'booking/booking_login.html')




@login_required
def booking_form(request):
    """
    To render the booking form after user logged in.
    User is able to book a session with choices.
    """

    if request.method == 'POST':
        form = BookingForm(data=request.POST)

        if form.is_valid():
            
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, f'Your booking is successful!')

        
            return redirect(f'/booking_success/{booking.id}/', kwargs={'pk': booking.id})

    form = BookingForm()


    return render(request, 'booking/booking_form.html', {'form': form})




class BookingTemplateView(TemplateView):
    """
    To display a list of bookings.
    """

    model = Booking
    fields = '__all__'
   
    template_name = 'booking/booking_detail.html'


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects.filter()
       

        return context




class BookingSuccessView(DetailView):
    """
    To render the booking data from the database.
    Display the bookings user has made.
    """

    model = Booking
    template_name = 'booking/booking_detail.html'

    def get_context_data(self, **kwargs):
        context = {'booking': kwargs['object']}

        return context
        

    





