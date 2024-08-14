from rest_framework import serializers
from .models import Recipe, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    category = CategorySerializer()
    
    class Meta:
        model = Recipe
        fields = '__all__'  # Use '__all__' to include all fields of the model

  