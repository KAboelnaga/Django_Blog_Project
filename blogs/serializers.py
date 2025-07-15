from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'content', 'category', 'created_at']
