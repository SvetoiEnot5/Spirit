# Generated by Django 4.2.6 on 2023-11-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_diagram_alter_coach_image_alter_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Diagram',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='coahes',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='description',
        ),
        migrations.AddField(
            model_name='gym',
            name='workouts',
            field=models.ManyToManyField(related_name='+', to='main.workouts'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='qualification',
            field=models.CharField(max_length=30, verbose_name='Специализация'),
        ),
    ]
