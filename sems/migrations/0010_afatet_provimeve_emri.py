# Generated by Django 2.0.4 on 2018-06-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0009_remove_afatet_provimeve_mundesite'),
    ]

    operations = [
        migrations.AddField(
            model_name='afatet_provimeve',
            name='emri',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
