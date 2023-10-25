# Generated by Django 4.2.6 on 2023-10-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя тренера')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('qualification', models.CharField(max_length=30, verbose_name='Квалификация')),
                ('experience', models.CharField(max_length=30, verbose_name='Опыт работы')),
            ],
        ),
    ]
