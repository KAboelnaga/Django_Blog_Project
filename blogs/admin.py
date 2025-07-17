from django.contrib import admin
from .models import Post, Category #ForbiddenWord


# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
# admin.site.register(ForbiddenWord)
