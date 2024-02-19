from django.db import models


class Category(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=100, unique=True)


class Recipes(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='static/book/images', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Ingredients(models.Model):

    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredients = models.TextField()


class Instructions(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    instruction = models.TextField()


# Create your models here.
