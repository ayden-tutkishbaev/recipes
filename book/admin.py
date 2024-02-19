from django.contrib import admin
from .models import *


class RecipeDisplay(admin.ModelAdmin):
    list_display = ['title', 'description', 'time', 'photo', 'category']


admin.site.register(Category)
admin.site.register(Recipes, RecipeDisplay)
admin.site.register(Ingredients)
admin.site.register(Instructions)



# Register your models here.
