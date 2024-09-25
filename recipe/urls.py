from django.urls import path
from .views import Recipes, RecipeDetail, RecipeComments, RecipeListByCategory, CategoryList, TimeOption, Serving, add_recipe, recipe_list, CommentCreateView , GetCSRFToken
from recipe import views

urlpatterns = [
    path('', views.index, name='index'),
    #127.0.0.1:800
    path('recipes/', Recipes.as_view(), name='recipe-list'),
    #127.0.0.1:8000/recipes path
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    #127.0.0.1:8000/recipes/id path
    path('recipes/<int:pk>/comments/', RecipeComments.as_view(), name='recipe-comments'),
    #127.0.0.1:8000/recipes/id/comments 
    path('recipes/add-comment/', CommentCreateView.as_view(), name='add-comment'),
    #127.0.0.1:8000/recipes/add-comments
    path('recipes/add/', add_recipe, name='add-recipe'),
    #127.0.0.1:8000/recipes/id/add
    path('recipes/search/', views.recipe_list, name='search-recipes'),
    #127.0.0.1:8000/recipes/search
    path('categories/', CategoryList.as_view(), name='category-list'),
    #127.0.0.1:8000/recipes/id/categories
    path('categories/<int:category_pk>/recipes', RecipeListByCategory.as_view(), name='recipe_list_by_category'),
    #127.0.0.1:8000/recipes/serving-options
    path('serving-options/', Serving.as_view(), name='serving-list'),
    #127.0.0.1:8000/recipes/prep-options
    path('prep-options/', TimeOption.as_view(), name='prep-list'),
    #127.0.0.1:8000/recipes/cook-options
    path('cook-options/', TimeOption.as_view(), name='cook-list'),
    path('csrf_cookie', GetCSRFToken.as_view()),
]


