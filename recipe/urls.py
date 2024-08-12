from operator import index
from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeComments
from recipe import views
from .views import add_recipe, recipe_list

urlpatterns = [
    path('', views.index, name='index'),
    #127.0.0.1:800
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    #127.0.0.1:8000/recipes path
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    #127.0.0.1:8000/recipes/id path
    path('recipes/<int:pk>/comments/', RecipeComments.as_view(), name='recipe-comments'),
    #127.0.0.1:8000/recipes/id/comments path
    path('add/', add_recipe, name='add-recipe'),
     #127.0.0.1:8000/recipes/id/add
    path('search/', recipe_list, name='search-recipes'),
    # 
]


