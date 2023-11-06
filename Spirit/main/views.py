from django.shortcuts import render, redirect
from django.contrib import messages
def alex(request):
    return render(request, 'main/index.html')

def coach(request):
    return render(request,'main/coach.html')
