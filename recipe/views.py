# Create your views here.
from rest_framework import generics
from .models import Recipe, Comment, Category, Servings, TimeOption
from .serializers import RecipeSerializer, CommentsSerializer, CategorySerializer, ServingsSerializer, TimeOptionSerializer
from django.shortcuts import render, redirect
from .forms import RecipeForm
from django.http import JsonResponse
from django.db.models import Q


def index(request):
    return render(request, 'index.html')

# Get Recipes
# ListCreateAPIView when you want to support both retrieving a list of objects and creating an object at the same endpoint without needing to write the code for both actions separately.
class Recipes(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

def add_recipe(request):
    if request.method == 'POST': #Checks if the form is being submitted (POST request).
        form = RecipeForm(request.POST, request.FILES) #Instantiates the form with the data from the POST request and any uploaded files.
        if form.is_valid(): #Validates the form data.
            form.save() #Saves the form data as a new recipe in the database.
            return redirect('recipe-list') #Redirects to list of all recipes after successfully adding a recipe.
    else:
        form = RecipeForm() 
    return render(request, 'add_recipe.html', {'form': form}) #Renders the add_recipe.html template, passing the form instance to the template context.

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

# Query time options
class TimeOption(generics.ListCreateAPIView):
    queryset = TimeOption.objects.all()
    serializer_class = TimeOptionSerializer

# Query serving amounts
class Servings(generics.ListCreateAPIView):
    queryset = Servings.objects.all()
    serializer_class = ServingsSerializer


