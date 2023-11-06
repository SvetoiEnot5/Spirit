from django.db import models
class Coach(models.Model):
    name = models.CharField('Имя тренера', max_length=30)
    age = models.IntegerField('Возраст')
    qualification = models.CharField('Квалификация',max_length=30)
    experience = models.CharField('Опыт работы',max_length=30)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Gym(models.Model):
    name = models.CharField('Название зала', max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField('Название абонемента', max_length=30)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    price = models.IntegerField('Цена')
    def __str__(self):
        return self.name + ' ' + self.price

class Client(models.Model):
    name = models.CharField('Имя клиента', max_length=30)
    age = models.IntegerField('Возраст')
    number = models.CharField('Номер телефона', max_length=20)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Request(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.client.name+ ' ' + self.card.name