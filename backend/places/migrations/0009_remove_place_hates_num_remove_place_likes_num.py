# Generated by Django 4.2.3 on 2023-07-08 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='hates_num',
        ),
        migrations.RemoveField(
            model_name='place',
            name='likes_num',
        ),
    ]
