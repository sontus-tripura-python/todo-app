from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm
# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'tasks': tasks, 'form': form }
    return render(request, 'todo/home.html', context)
def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form }
    return render(request, 'todo/update.html', context)
def deletetask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task': task }
    return render(request, 'todo/delete.html', context)
