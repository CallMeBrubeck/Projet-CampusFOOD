# Generated by Django 5.0.3 on 2024-05-20 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfoodapp', '0004_restaurant_directeur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis',
            name='note',
        ),
    ]