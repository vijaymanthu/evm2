# Generated by Django 3.0 on 2021-11-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_newuser_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]