from django.db import models
from django.utils import timezone

class Post(models.Model):
    ID=models.AutoField(primary_key=True,editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title