from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment
from blogs.models import Post


@login_required
def add_comment(request, post_id, parent_id=None):
    post = get_object_or_404(Post, id=post_id)
    parent_comment = Comment.objects.filter(ID=parent_id).first() if parent_id else None

   

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                
                USER_ID = request.user_ID,
                POST_ID = post_id,
                PARENT_COMMENT_ID = parent_id,
                CONTENT = form.cleaned_data['content']
               
            )
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})