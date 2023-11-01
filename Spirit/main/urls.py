from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.alex, name='home'),
    path('', views.alex, name='home'),
    path('coach', views.coach, name='coach'),
]
