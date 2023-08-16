# Generated by Django 4.2.2 on 2023-07-03 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('likes_num', models.PositiveIntegerField()),
                ('hates_num', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]