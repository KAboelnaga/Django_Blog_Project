from django.db import models
from django.conf import settings
from blogs.models import Category

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'category')

    def __str__(self):
        return f'{self.user.username} subscribed to {self.category.name}'
