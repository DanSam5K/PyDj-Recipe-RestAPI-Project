"""
Serializers for recipe app APIS
"""
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe object"""
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'link',
                  'description')
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail object"""
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ('description',)
