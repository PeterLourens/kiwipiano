from django.shortcuts import render, redirect
from django.views import generic
from .models import Lesson
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages


# render the home page
def home(request):

    context = {
        'lessons': Lesson.objects.all()
    }
    return render(request, 'index.html', context)



# render the account register page
def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account registration is successful!')

            return redirect('feedback')
            
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def feedback(request):
    return render(request, 'register_feedback.html')

