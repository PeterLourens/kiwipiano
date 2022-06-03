from django.shortcuts import render
from django.views import generic
from .models import Lesson
from django.contrib.auth.forms import UserCreationForm


# class LessonView(generic.ListView):
#     model = Lesson
#     queryset = Lesson.objects.filter(status=1).order_by('-start_time')
#     template_name = 'index.html'
#     paginate_by = 2



def home(request):

    context = {
        'lessons': Lesson.objects.all()
    }
    return render(request, 'index.html', context)



def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_multipart():
            username = form.cleaned_data.get('username')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'title': 'Register'})

