from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page_view, name='category_page'),
    path('about_us/', about_us_page_view, name='about_us'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail')   # Not working
]


