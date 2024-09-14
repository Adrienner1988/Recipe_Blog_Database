from rest_framework import serializers
from .models import Recipe, Comment, Category, Serving, TimeOption

class TimeOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOption
        fields = ['id', 'time']

class ServingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serving
        fields = ['id', 'serving']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = ['id', 'text', 'created_at', 'recipe']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['recipe','text']
        
class RecipeSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    category = CategorySerializer()
    prep = TimeOptionSerializer()
    cook= TimeOptionSerializer()
    serving = ServingSerializer()
 
    class Meta:
        model = Recipe
        fields = ['title', 'prep', 'cook', 'serving', 'category', 'ingredients', 'steps', 'image', 'comments']
        

class RecipeCreateSerializer(serializers.ModelSerializer):
    prep = serializers.PrimaryKeyRelatedField(queryset=TimeOption.objects.all())
    cook= serializers.PrimaryKeyRelatedField(queryset=TimeOption.objects.all())
    serving = serializers.PrimaryKeyRelatedField(queryset=Serving.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Recipe
        fields = ['title', 'prep', 'cook', 'serving', 'category', 'ingredients', 'steps', 'image']

  