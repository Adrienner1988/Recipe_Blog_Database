from django.urls import path
from .views import RecipeList, RecipeDetail

urlpatterns = [
    path('recipe/', RecipeList.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]
