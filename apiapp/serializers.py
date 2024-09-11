from rest_framework import serializers
from .models import Recipes

class Recipeserializer(serializers.ModelSerializer):
    recipe_Image = serializers.ImageField(required=False)
    class Meta:
        model = Recipes
        fields = '__all__'
