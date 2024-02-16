from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()
    recipes = Recipes.objects.all()

    context = {
        'title': 'Главная страница',
        'categories': categories,
        'recipes': recipes
    }

    return render(request, 'recipesbook/index.html', context)