from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from .forms import ProfileForm

def alex(request):
    return render(request, 'main/index.html')


def coach(request):
    return render(request, 'main/coach.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('login')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('/register')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "Phone Number is Taken")
                return redirect('/register')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "User is Created Please Login")
        return redirect('/register')

    return render(request, "main/register.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')

    return render(request, "main/login.html")


def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/')
def profile(request):
    return render(request, 'main/profile.html')
# views.py

# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if  profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, 'Ваш профиль был успешно обновлен!')
#             return redirect('settings:profile')
#         else:
#             messages.error(request, 'Пожалуйста, исправьте ошибки.')
#     else:
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, '/profile.html', {
#         'profile_form': profile_form
#     })