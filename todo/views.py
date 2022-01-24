from django.shortcuts import render
from django.http import HttpResponse
from todo.models import *

def todopage(request):
    tasks = Task.objects.all()
    context={'tasks':tasks}
    return render(request,'tasks.html', context )
