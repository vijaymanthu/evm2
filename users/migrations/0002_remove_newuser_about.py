# Generated by Django 3.0 on 2021-11-28 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='about',
        ),
    ]
