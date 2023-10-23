from django.shortcuts import render
from django.http import HttpResponse
def alex(request):
    return HttpResponse("<h4>Тимофей пидор</h4>")
def artur(request):
    return HttpResponse("<h4>Артур спидраннер</h4>")