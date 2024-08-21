# Generated by Django 5.0.7 on 2024-08-21 02:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_rename_size_servings_serving_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipe.category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cook_time', to='recipe.timeoption'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='prep_time', to='recipe.timeoption'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='servings', to='recipe.servings'),
        ),
    ]
