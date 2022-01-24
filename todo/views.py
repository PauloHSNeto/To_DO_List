from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import *
from todo.forms import *


def todopage(request):
    tasks = Task.objects.all()
    forms = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context={'tasks':tasks, 'forms':forms}
    return render(request,'tasks.html', context )
