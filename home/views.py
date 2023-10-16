from django.shortcuts import render
from rest_framework import viewsets
from django.core.paginator import Paginator
from .serializers import ProjectSerializer
from .models import Project

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

def home_pg(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/index.html', context={'page_obj': page_obj})
