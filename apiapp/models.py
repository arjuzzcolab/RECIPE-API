from django.db import models
from datetime import timedelta

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=200)
    preparation_Time = models.DurationField(default=timedelta(minutes=120))
    difficulty_choices = [
        (1,'Easy'),(2,'Medium'),(3,'Hard')
    ]
    difficulty = models.IntegerField(choices=difficulty_choices)
    recipe = models.TextField()
    recipe_Image = models.ImageField(upload_to='recipe_media')
    vegetarian = models.BooleanField()