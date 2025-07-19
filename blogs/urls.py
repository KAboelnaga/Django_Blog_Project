from django.urls import path
from . import views
from .views import PostListCreateAPIView, PostDetailAPIView


app_name = 'blogs'

urlpatterns = [
    
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_edit'), 
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('categories/', views.category_list, name='categories_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('api/posts/', PostListCreateAPIView.as_view(), name='api-post-list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-post-detail'),
    path('api/like/<int:post_id>/', views.like_post, name='like_post'),

]



