from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import UpdateView
from .forms import UpdateProfileForm, UpdateUserForm

from .models import Profile

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
    username=request.user
    posts=User.objects.filter(username= username)
    profile=Profile.objects.filter(user=username)
    context={'posts':posts,'profile':profile}
    return render(request, 'main/profile.html',context)

@login_required()
def update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return redirect('/profile')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'main/update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
# class UpdateProfile(UpdateView):
#     model = User
#     model1 = Profile
#     template_name = 'main/update.html'
#     form_class = UpdateProfileForm
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