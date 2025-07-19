from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment
from blogs.models import Post
from .forms import CommentForm
from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer


def get_all_comments(request,post_id):
    comments = Comment.objects.filter(POST=post_id,PARENT_COMMENT__isnull=True)
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm()
    print("posttttttttttt", post.id)
    for comment in comments:
        print("commentcomment",comment.ID)
    return render(request, 'comments/comments_section.html', {'form': form, 'comments': comments, 'post': post})


@login_required
def add_comment(request, post_id, parent_id=None):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    parent_comment = Comment.objects.filter(ID=parent_id).first() if parent_id else None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                USER=user,
                POST=post,
                PARENT_COMMENT=parent_comment,
                CONTENT=form.cleaned_data['CONTENT']
            )

            #return redirect('blogs:post_detail', post_id=post.id)
            return redirect(f"/post/{post_id}?show_comments=true")

    else:
        form = CommentForm()

    return redirect('blogs:post_detail', post_id=post.id)

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(POST_ID=post_id).order_by('-CREATED_AT')

    def perform_create(self, serializer):
        serializer.save(POST_ID_id=self.kwargs['post_id'])