from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from comments.forms import CommentForm
from comments.models import Comment
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

def home(request):
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()

    return render(request, 'blogs/home.html', {
        'page_obj': page_obj,
        'categories': categories
    })

def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()

    return render(request, 'blogs/home.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category,
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(POST=post_id,PARENT_COMMENT__isnull=True)
    for comment in comments:
        print("comment IDdddddddddd:", comment.ID)

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.post = post
    #         comment.save()
    #         return redirect('blogs:post_detail', post_id=post.id)
    # else:
    form = CommentForm()
    return render(request, 'blogs/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,  # <-- pass the instance, not the class
    })

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
