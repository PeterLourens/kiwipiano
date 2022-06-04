from django.shortcuts import render
from django.views import generic
from .models import Lesson
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages



def home(request):

    context = {
        'lessons': Lesson.objects.all()
    }
    return render(request, 'index.html', context)



def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account registration is successful!')
            
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})
