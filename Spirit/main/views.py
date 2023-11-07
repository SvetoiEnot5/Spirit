from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
def alex(request):
    return render(request, 'main/index.html')

def coach(request):
    return render(request,'main/coach.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main/index.html')  # Перенаправьте на вашу главную страницу
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main/index.html')  # Перенаправьте на вашу главную страницу
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})