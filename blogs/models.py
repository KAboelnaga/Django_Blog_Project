from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts_images/', blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ForbiddenWord(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word