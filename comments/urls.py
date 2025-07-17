from django.urls import path
from .views import add_comment, CommentListCreateAPIView, get_all_comments

app_name = 'comments'

urlpatterns = [
    # path('api/posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='api-post-comments'),
    path('api/posts/<int:post_id>/comments/', get_all_comments, name='get_all_comments'),
    path('<int:post_id>/add/', add_comment, name='add_comment'),
    path('<int:post_id>/reply/<int:parent_id>/', add_comment, name='reply_comment'),
]
