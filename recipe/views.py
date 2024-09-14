# Create your views here.
from rest_framework import generics, permissions
from .models import Recipe, Comment, Category, Serving, TimeOption
from .serializers import RecipeSerializer, CommentsSerializer, CategorySerializer, ServingSerializer, TimeOptionSerializer, RecipeCreateSerializer, CommentCreateSerializer
from django.shortcuts import render, redirect
from .forms import RecipeForm, CommentForm
from django.http import JsonResponse
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')


# View for listing and creating recipes
class Recipes(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    
    
# Use different serializers for GET (list) and POST (create)
def get_serializer_class(self):
        if self.request.method == 'POST':
            return RecipeCreateSerializer  # Use this for form submissions
        return RecipeSerializer  # Use this for listing/viewing

# Function to post recipe
def add_recipe(request):
    if request.method == 'POST': # Checks if the form is being submitted (POST request).
        form = RecipeForm(request.POST, request.FILES) # Instantiates the form with the data from the POST request and any uploaded files
        print(request.POST)  # Log form data
        print(request.FILES)  # Log file 
        if form.is_valid(): # Validates the form data
            form.save() # Saves the form data as a new recipe in the database
            return redirect('recipe-list') # Redirects to list of all recipes after successfully adding a recipe.
    else:
        form = RecipeForm() 
    return render(request, 'add_recipe.html', {'form': form}) # Renders the add_recipe.html template, passing the form instance to the template context.


# View for fetching, updating, and deleting a specific recipe
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk' 
    
    
# Function to allow user to search recipes 
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
            "ingredients": recipe.ingredients.splitlines(),
            "steps": recipe.steps.splitlines(),
            "image": recipe.image.url if recipe.image else None,
        }
        for recipe in recipes
    ]
    
    return JsonResponse(recipe_data, safe=False)


# View for querying recipe categories
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# View for querying recipes by category
class RecipeListByCategory(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Recipe.objects.filter(category_id=category_id)


# View for querying time options
class TimeOption(generics.ListCreateAPIView):
    queryset = TimeOption.objects.all()
    serializer_class = TimeOptionSerializer


# View for querying serving sizes
class Serving(generics.ListCreateAPIView):
    queryset = Serving.objects.all()
    serializer_class = ServingSerializer
   

 # View for handling recipe comments
class RecipeComments(generics.ListAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        recipe_id = self.kwargs['pk']
        return Comment.objects.filter(recipe_id=recipe_id)
    
    
 # View for creating recipe comments
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
 
    
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return render('recipe-detail')
        else:
            form = CommentForm()
        return render(request, 'add_comment.html', {'form': form})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response( {'success': 'CSRF cookie set'})
