from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Coach(models.Model):
    name = models.CharField('Имя тренера', max_length=30)
    age = models.IntegerField('Возраст')
    qualification = models.CharField('Специализация', max_length=30)
    experience = models.CharField('Опыт работы', max_length=30)
    image = models.ImageField(null=True, blank=True, upload_to='coachs/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Workouts(models.Model):
    name = models.CharField('Название тренировки', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'


class Gym(models.Model):
    name = models.CharField('Название зала', max_length=30)
    workouts = models.ManyToManyField(Workouts, related_name='+')
    price = models.IntegerField('Цена', null=True)
    image = models.ImageField(null=True, blank=True, upload_to='coachs/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class CardPlan(models.Model):
    duration = models.CharField('Длительность', max_length=30)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.duration

    class Meta:
        verbose_name = 'План абонемента'
        verbose_name_plural = 'Планы абонементов'


class Card(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    duration = models.ForeignKey(CardPlan, on_delete=models.CASCADE, blank=True, null=True)
    IssueDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    price = models.IntegerField('Цена')
    is_payed = models.BooleanField('Статус оплаты', blank=True, default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='coachs/')

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
