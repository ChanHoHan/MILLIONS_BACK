# Generated by Django 2.2.7 on 2019-11-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimerPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='time',
            field=models.CharField(max_length=30),
        ),
    ]
