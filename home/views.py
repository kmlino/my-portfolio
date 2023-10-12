from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Project

def home_pg(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/index.html', context={'page_obj': page_obj})


def about(request):
    return render(request, 'home/about.html')


# def my_work(request):
#     return render(request, 'home/projects.html')


def project(request):
    pass
    # projects = Project.objects.all()
    # return render(request, 'home/projects.html', context={'projects': projects})
