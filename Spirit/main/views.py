from django.shortcuts import render
from django.http import HttpResponse
def alex(request):
    return render(request, 'main/index.html')

def artur(request):
    return render(request, 'main/about.html')