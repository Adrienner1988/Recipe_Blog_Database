from django.contrib import admin
from .models import Recipe, Comment, Category, TimeOption, Servings

admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(TimeOption)
admin.site.register(Servings)