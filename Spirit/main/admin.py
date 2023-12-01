from django.contrib import admin
from django.shortcuts import render

from .models import Coach, Card, Gym, Profile, CardPlan, Workouts, Schedule

admin.site.register(Coach)
admin.site.register(Card)
admin.site.register(Gym)
admin.site.register(Profile)
admin.site.register(CardPlan)
admin.site.register(Workouts)
admin.site.register(Schedule)
