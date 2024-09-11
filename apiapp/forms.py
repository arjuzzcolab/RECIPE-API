from .models import Recipes
from django import forms

class Recipeform(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter recipe name'}),
            'preparation_Time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM:SS'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'recipe': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter description'}),
            'recipe_Image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'vegetarian': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        