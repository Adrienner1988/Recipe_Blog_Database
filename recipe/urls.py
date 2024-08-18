from operator import index
from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeComments, RecipeListByCategory, CategoryList
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
    path('recipes/add/', add_recipe, name='add-recipe'),
    #127.0.0.1:8000/recipes/id/add
    path('recipes/search/', recipe_list, name='search-recipes'),
    #127.0.0.1:8000/recipes/search
    path('categories/', CategoryList.as_view(), name='category-list'),
    #127.0.0.1:8000/recipes/id/categories
    path('categories/<int:category_pk>/recipes', RecipeListByCategory.as_view(), name='recipe_list_by_category'),
    #127.0.0.1:8000/recipes/serving-options
    path('servings-options/', views.ServingsListView.as_view(), name='servings-list'),
    #127.0.0.1:8000/recipes/prep-options
    path('prep-options/', views.TimeOptionPrepListView.as_view(), name='prep-list'),
    #127.0.0.1:8000/recipes/cook-options
    path('cook-options/', views.TimeOptionCookListView.as_view(), name='cook-list'),
]


