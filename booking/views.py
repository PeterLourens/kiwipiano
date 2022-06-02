from django.shortcuts import render
from django.views import generic
from .models import Lesson



class LessonView(generic.ListView):
    model = Lesson
    queryset = Lesson.objects.filter(status=1).order_by('-start_time')
    template_name = 'index.html'
    paginate_by = 2

