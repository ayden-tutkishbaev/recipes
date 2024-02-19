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


def category_page_view(request, category_id):
    recipes = Recipes.objects.filter(id=category_id)

    context = {
        'title': Category.objects.filter(id=category_id),
        'recipes': recipes
    }

    return render(request, 'recipesbook/category_page.html', context)


def about_us_page_view(request):
    return render(request, 'recipesbook/about_us.html')


def recipe_detail(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)

    ingredients = Category.objects.all()
    instructions = Instructions.objects.all()

    context = {
        'title': f'{recipe.title}',
        'article': recipe,
        'ingredients': ingredients,
        'instructions': instructions
    }

    return render(request, 'recipesbook/recipe_detail.html', context)