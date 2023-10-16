from django.urls import path, include
from . import views
from rest_framework import routers, serializers, viewsets
from home import views

urlpatterns = [
    path('', views.home_pg, name="home"),
    path('about/', views.about, name="about" ),
    path('project/', views.project, name="project" ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
