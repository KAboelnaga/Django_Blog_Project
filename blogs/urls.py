
from django.urls import path
from . import views
from .views import PostListCreateAPIView, PostDetailAPIView

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    path('api/posts/', PostListCreateAPIView.as_view(), name='api-post-list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-post-detail'),
]
