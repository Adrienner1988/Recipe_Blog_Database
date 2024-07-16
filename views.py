# Create your views here.
from rest_framework import generics
from .models import Recipe, Comment
from .serializers import RecipeSerializer, CommentsSerializer
from django.shortcuts import render
# from django.http import HttpResponse 

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