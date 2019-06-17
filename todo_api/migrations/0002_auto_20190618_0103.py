# Generated by Django 2.2.2 on 2019-06-17 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_due',
        ),
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_creation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
