from django.shortcuts import render, redirect
from .models import Demo
from .forms import Demoform

def index(request):
    demos = Demo.objects.order_by('-date_posted')

    context = {'demos' : demos}

    return render(request, 'demo/index.html', context)

def add(request):
    if request.method == 'POST':
        form = Demoform(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = Demoform()
        

    context = {'form' : form}

    return render(request, 'demo/add.html', context)