from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class TimeOption(models.Model):
    value = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.value
    
class Servings(models.Model):
    size = models.CharField(max_length=20, unique=True)
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(upload_to='recipe/images/', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE, null=True, blank=True) 
    prep = models.ForeignKey(TimeOption, related_name='prep_time', on_delete=models.CASCADE, null=True, blank=True)
    cook = models.ForeignKey(TimeOption, related_name='cook_time', on_delete=models.CASCADE, null=True, blank=True)
    servings = models.ForeignKey(Servings, related_name='servings', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

