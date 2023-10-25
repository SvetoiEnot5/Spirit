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