from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment
from blogs.models import Post
from .forms import CommentForm
from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer



def add_comment(request, post_id, parent_id=None):
    print("helllllo",parent_id)
    post = get_object_or_404(Post, id=post_id)
    parent_comment = Comment.objects.filter(ID=parent_id).first() if parent_id else None
    
   

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                POST_ID = post,
                PARENT_COMMENT_ID = parent_comment,
                CONTENT = form.cleaned_data['CONTENT']
               
            )
            return redirect('blogs:post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(POST_ID=post_id).order_by('-CREATED_AT')

    def perform_create(self, serializer):
        serializer.save(POST_ID_id=self.kwargs['post_id'])