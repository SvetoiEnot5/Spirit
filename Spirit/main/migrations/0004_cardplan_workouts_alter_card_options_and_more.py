# Generated by Django 4.2.6 on 2023-11-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_remove_request_card_remove_request_client_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField(verbose_name='Длительность')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название тренировки')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Абонемент', 'verbose_name_plural': 'Абонементы'},
        ),
        migrations.AlterModelOptions(
            name='coach',
            options={},
        ),
        migrations.AlterModelOptions(
            name='gym',
            options={'verbose_name': 'Зал', 'verbose_name_plural': 'Залы'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='gym',
            name='coahes',
            field=models.ManyToManyField(to='main.coach'),
        ),
    ]
