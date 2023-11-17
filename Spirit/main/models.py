from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Coach(models.Model):
    name = models.CharField('Имя тренера', max_length=30)
    age = models.IntegerField('Возраст')
    qualification = models.CharField('Квалификация', max_length=30)
    experience = models.CharField('Опыт работы', max_length=30)

    def __str__(self):
        return self.name

    def filter_coach(self):
        return Coach.object.order_by('name')
    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Gym(models.Model):
    name = models.CharField('Название зала', max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

class Card(models.Model):
    name = models.CharField('Название абонемента', max_length=30)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name + ' ' + self.price


    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# class Request(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     card = models.ForeignKey(Card, on_delete=models.CASCADE)
#     status = models.BooleanField(default=False)
#     def __str__(self):
#         return self.client.name+ ' ' + self.card.name
