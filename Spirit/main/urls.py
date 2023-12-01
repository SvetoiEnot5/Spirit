from django.urls import path, include
from .views import alex, coach, register, handlelogin, handlelogout, profile, update, gym, card, CoachView, stat, get_schedule

urlpatterns = [
    path('home', alex, name='home'),
    path('', alex, name='home'),
    path('coach', coach, name='coach'),
    path('gym', gym, name='gym'),
    path('register', register, name='register'),
    path('login', handlelogin, name='auth'),
    path('logout', handlelogout, name='exit'),
    path('profile', profile, name='profile'),
    path('update', update, name='update'),
    path('card', card, name='card'),
    path('stat', stat, name='stat'),
    path('get_schedule', get_schedule, name='get_schedule'),
    path('<int:pk>', CoachView.as_view(), name='coachview')
]
