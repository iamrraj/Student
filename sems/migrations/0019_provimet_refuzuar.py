# Generated by Django 2.0.4 on 2018-06-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0018_provimet_afati'),
    ]

    operations = [
        migrations.AddField(
            model_name='provimet',
            name='refuzuar',
            field=models.BooleanField(default=False),
        ),
    ]
