from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField('Tags', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogs:post_detail', args=[str(self.id)])

class Like(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('blogs.Post', on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)

class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name