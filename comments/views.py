from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment
from blogs.models import Post
from .forms import CommentForm



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