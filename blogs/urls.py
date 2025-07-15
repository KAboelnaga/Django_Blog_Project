from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),  # homepage with pagination
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]