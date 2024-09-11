# Generated by Django 4.2.15 on 2024-09-09 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('preparation_Time', models.DurationField(default=datetime.timedelta(seconds=7200))),
                ('difficulty', models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])),
                ('recipe', models.TextField()),
                ('recipe_Image', models.ImageField(upload_to='recipe_media')),
                ('vegetarian', models.BooleanField()),
            ],
        ),
    ]
