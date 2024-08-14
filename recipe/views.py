# Create your views here.
from rest_framework import generics
import recipe
from .models import Recipe, Comment, Category
from .serializers import RecipeSerializer, CommentsSerializer, CategorySerializer
from django.shortcuts import render, redirect
from .forms import RecipeForm
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

# Get Recipes
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# Get the details of the recipes by the pk/id
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk' 

# Get the recipe comments by the pk/id
class RecipeComments(generics.ListAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        recipe_id = self.kwargs['pk']
        return Comment.objects.filter(recipe_id=recipe_id)

# Allow user to add a recipe
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
        else:
            form = RecipeForm()
        return render(request, 'add_recipe.html', {'form': form})
    
#Allow user to search recipes 
def recipe_list(request):
    title_query = request.GET.get('title', '')
    ingredient_query = request.GET.get('ingredient', '')
    category_query = request.GET.get('category', '')

    filters = Q()
    if title_query:
        filters &= Q(title__icontains=title_query)
    if ingredient_query:
        filters &= Q(ingredients__icontains=ingredient_query)
    if category_query:
        filters &= Q(category_id=category_query)

    # Filter recipes based on constructed filters
    recipes = Recipe.objects.filter(filters).distinct()

    # Prepare the recipe data to be returned
    recipe_data = [
        {
            "id": recipe.id,
            "title": recipe.title,
            "ingredients": recipe.ingredients.splitlines(),  # Split by new lines
            "steps": recipe.steps.splitlines(),  # Split by new lines
            "image": recipe.image.url if recipe.image else None,
        }
        for recipe in recipes
    ]
    
    return JsonResponse(recipe_data, safe=False)

# Query recipe categories
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecipeListByCategory(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Recipe.objects.filter(category_id=category_id)