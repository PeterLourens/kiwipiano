from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Profile, Booking


from .forms import (
    UserRegisterForm, 
    UserProfileForm, 
    ProfileUpdateForm,
    ProfileDeleteForm,
    BookingForm,
)

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin



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

    context = {
        'form': form,
        'title': 'Register'
    }

    return render(request, 'account/signup.html', context)



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


    return render(request, 'account/login.html', {'title': 'Login'})



def logout_view(request):
    """
    To render the home page after user logged out the account.
    """

    logout(request)

    return render(request, 'index.html', {'title': 'Logout'})



def feedback(request):
    """
    To render the registration feedback view after 
    user registered on the register view.
    """
    return render(request, 'account/register_feedback.html', {'title': 'Register'})


@login_required
def profile(request):
    """
    To render the user profile page with user's personal information.
    """
    my_bookings = Booking.objects.filter(user=request.user)

    context = {
        'my_bookings': my_bookings,
        'title': 'Profile'

    }

    return render(request, 'profile/profile.html', context)
   
   

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
        'title': 'Profile'
      
    }
   
    return render(request, 'profile/update_profile.html', context)



def delete_profile(request):
    """
    To delete the user profile and associated data from the database.
    To return to the home page after user deletes his/her profile.
    """

    if request.method == 'POST':
        delete_profile = ProfileDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()

        messages.success(request,  f'Your profile has been deleted!')
        return redirect('home')

    else:
        delete_profile = ProfileDeleteForm(instance=request.user)

    return render(request, 'profile/delete_profile.html')



def booking_login(request):
    """
    To render the booking login alert page. When user clicks the booking btn,
    it asks user to login or register an account first.
    """

    return render(request, 'booking/booking_login.html', {'title': 'Login'})



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
           
            return redirect('profile')

    else:
        form = BookingForm()


    context = {
        'form': form,
        'title': 'Booking'
    }


    return render(request, 'booking/booking_form.html', context)




class BookingDetailView(DetailView):
    """
    To display the bookings details.
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
        

class BookingUpdateView(SuccessMessageMixin, UpdateView):
    """
    To render the booking details that user has made.
    """

    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_update.html'
    success_message = 'Your booking has been updated!'

    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']
        
        return reverse('booking_detail', kwargs={'pk': self.kwargs['pk']})



class BookingUpdateSuccessView(DetailView):
    """
    To render the booking details after updating .
    Display the booking updates user has made.
    """

    model = Booking
    template_name = 'booking/booking_update_success.html'

    def get_context_data(self, **kwargs):
        context = {'booking': kwargs['object']}

        return context
        


def booking_delete(request, pk):
    """
    To render the booking delete page, 
    and delete the booking in the database.
    """
    booking = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, f'Your booking has been deleted!')
        return redirect('profile')


    return render(request, 'booking/booking_delete.html', {'booking': booking})


