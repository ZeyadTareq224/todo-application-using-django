from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


@login_required(login_url='login')
def index(request):
	user = request.user
	tasks = user.task_set.all()
	form = TaskForm()

	if (request.method == 'POST'):
		form = TaskForm(request.POST)
		if (form.is_valid()):
			form.instance.user = user
			form.save()
		return 	redirect('/')
	context = {'tasks': tasks, 'form': form}
	return render(request, 'tasks/list.html', context)


@login_required(login_url='login')
def update_task(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)

	if(request.method == 'POST'):
		form = TaskForm(request.POST, instance=task)

		if(form.is_valid()):
			form.save()
			return redirect('/')

	context = {'form': form}

	return render(request, 'tasks/update_tasks.html', context)


@login_required(login_url='login')
def delete(request, pk):
	item = Task.objects.get(id=pk)
	if(request.POST):
		item.delete()
		return redirect('/')
	context = {'item': item}
	return render(request, 'tasks/delete.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegistrForm()
    return render(request, 'tasks/register.html', {'form': form})