from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.


def home_pg(request):
    projects = Project.objects.all()
    return render(request, 'home/index.html', context={'projects': projects})
    # return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def my_work(request):
    return render(request, 'home/projects.html')


def project(request):
    projects = Project.objects.all()
    return render(request, 'home/project.html', context={'projects': projects})
