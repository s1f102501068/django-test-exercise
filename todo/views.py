from django.shortcuts import render
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

