# Generated by Django 3.2.5 on 2021-12-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20211128_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinfo',
            name='description',
            field=models.CharField(max_length=1026, null=True),
        ),
    ]
