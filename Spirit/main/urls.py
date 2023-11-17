from django.urls import path, include
from .views import alex,coach,register, handlelogin, handlelogout,profile,update, filter_coaches


urlpatterns = [
    path('home', alex, name='home'),
    path('', alex, name='home'),
    path('coach', coach, name='coach'),
    path('filter_coach', filter_coaches, name='filter_coach'),
    path('register', register, name='register'),
    path('login', handlelogin, name='auth'),
    path('logout', handlelogout, name='exit'),
    path('profile', profile, name='profile'),
    path('update', update, name='update')
]
