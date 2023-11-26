from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UpdateProfileForm, UpdateUserForm
from .models import Profile, Coach, Gym, CardPlan, Card
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView


def alex(request):
    return render(request, 'main/index.html')


def coach(request):
    coaches = Coach.objects.all()[:3]
    tren = Coach.objects.all()[3:]
    context = {"coaches": coaches,
               "tren": tren}
    return render(request, 'main/coach.html', context)


def gym(request):
    gym = Gym.objects.all()[:1]
    tren = Gym.objects.all()[1:]
    context = {"gym": gym,
               "tren": tren}
    return render(request, 'main/gym.html', context)


def register(request):
    if request.method == "POST":
        username = request.POST.get('login')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.info(request, "Пароли не совпадают")
            return redirect('/register')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "Логин занят")
                return redirect('/register')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "Пользователь создан")
        return redirect('/login')

    return render(request, "main/register.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Вы успешно вошли")
            return redirect('/')
        else:
            messages.error(request, "Неправильные данные")
            return redirect('/login')

    return render(request, "main/login.html")


def handlelogout(request):
    logout(request)
    messages.success(request, "Вы успешно вышли")
    return redirect('/')


def profile(request):
    username = request.user
    posts = User.objects.filter(username=username)
    profile = Profile.objects.filter(user=username)
    cards = Card.objects.filter(user=username)
    context = {'posts': posts, 'profile': profile, 'cards': cards}
    return render(request, 'main/profile.html', context)


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
        username = request.user
        gym = Gym.objects.all()
        coach = Coach.objects.all()
        plan = CardPlan.objects.all()
        if Card.objects.filter(user=username):
            messages.warning(request, "У вас есть абонемент")
            return redirect('/profile')
        else:
            if request.method == "POST":
                hall_id = request.POST.get('gym')
                trainer_id = request.POST.get('coach')
                duration_id = request.POST.get('plan')
                price = request.POST.get('price')
                hall = get_object_or_404(Gym, name=hall_id)
                trainer = get_object_or_404(Coach, name=trainer_id)
                duration = get_object_or_404(CardPlan, duration=duration_id)
                query = Card(user=request.user, gym=hall, coach=trainer, duration=duration, price=price)
                query.save()
                messages.success(request, "Вы оформили абонемент")
                return redirect('/card')
        return render(request, 'main/card.html', {
            'gym': gym,
            'coach': coach,
            'plan': plan,
        })
    else:
        return redirect('/login')

class CoachView(DetailView):
    model = Coach
    template_name = 'main/coach_view.html'
    context_object_name = 'coach'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        coach = self.get_object()

        coach_cards = Card.objects.filter(coach=coach)

        context['coach_cards'] = coach_cards

        return context


def stat(request):
    subscriptions = Card.objects.all()
    # Подготовка данных для круговой диаграммы
    durations = [card.duration.duration for card in subscriptions]
    unique_durations = list(set(durations))
    data = [durations.count(duration) for duration in unique_durations]
    context = {
        'labels': unique_durations,
        'data': data,
    }

    return render(request, 'main/stat.html', context)