from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import UpdateProfileForm, UpdateUserForm
from .models import Profile, Coach, Gym, CardPlan, Card
from django.shortcuts import get_object_or_404

def alex(request):
    return render(request, 'main/index.html')


def coach(request):
    coaches = Coach.objects.all()[:3]
    tren = Coach.objects.all()[3:]
    context = {"coaches": coaches,
               "tren": tren}
    return render(request, 'main/coach.html', context)
def gym(request):
    gym = Gym.objects.all()[:3]
    tren = Gym.objects.all()[3:]
    context = {"coaches": gym,
               "tren": tren}
    return render(request, 'main/gym.html', context)

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
    cards=Card.objects.filter(user=username)
    print(cards)
    context={'posts':posts,'profile':profile, 'cards':cards}
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

def card(request):
    if request.user.is_authenticated:
        gym = Gym.objects.all()
        coach = Coach.objects.all()
        plan = CardPlan.objects.all()
        if request.method == "POST":
            hall_id = request.POST.get('gym')
            trainer_id = request.POST.get('coach')
            duration_id = request.POST.get('plan')
            print(duration_id)
            price = request.POST.get('price')
            hall = get_object_or_404(Gym, name=hall_id)
            trainer = get_object_or_404(Coach, name=trainer_id)
            duration = get_object_or_404(CardPlan, duration=duration_id)
            query = Card(user=request.user, gym=hall, coach=trainer, duration=duration, price=price)
            query.save()
            messages.success(request, "Вы оформили абонемент")
            return redirect('/card')
    return render(request,'main/card.html', {
        'gym': gym,
        'coach': coach,
        'plan': plan,
    })