from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.alex),
    path('Артур', views.artur)
]
