# Create your views here.
from rest_framework import generics
from .models import Recipe, Comment
from .serializers import RecipeSerializer, CommentsSerializer
from django.shortcuts import render, redirect
from .forms import RecipeForm

def index(request):
    return render(request, 'index.html')

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk' 

class RecipeComments(generics.ListAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        recipe_id = self.kwargs['pk']
        return Comment.objects.filter(recipe_id=recipe_id)
    
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail')
        else:
            form = RecipeForm()
        return render(request, 'add_recipe.html', {'form': form})