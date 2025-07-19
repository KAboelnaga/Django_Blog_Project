import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Like
from comments.forms import CommentForm
from comments.models import Comment
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .forms import PostForm, CategoryForm
from django.contrib import messages
from django.contrib.auth import get_user_model

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

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
    likesInfo =get_likes_details(post_id, request.user.id) if request.user.is_authenticated else None
    form = CommentForm()
    return render(request, 'blogs/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form, 
        'likesInfo':likesInfo 
    })

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   




def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blogs/posts_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts_list') 
    else:
        form = PostForm()
    return render(request, 'blogs/post_create.html', {'form': form})
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/post_create.html', {'form': form})
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blogs:posts_list')
    return render(request, 'blogs/post_confirm_delete.html', {'post': post})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blogs/categories_list.html', {'categories': categories})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blogs:categories_list')
    return render(request, 'blogs/category_form.html', {'form': form})


def category_update(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        return redirect('blogs:categories_list')
    return render(request, 'blogs/category_form.html', {'form': form})


def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect('blogs:categories_list')
    return render(request, 'blogs/category_confirm_delete.html', {'cat': cat})





@login_required
@require_http_methods(["POST", "DELETE"])
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    body_data = json.loads(request.body.decode('utf-8'))
    is_liked = body_data.get('is_liked')
    print("Like Data:", is_liked)
    
    if request.method == "POST":
        # Remove opposite reaction before adding new one
        Like.objects.filter(user=user, post=post).delete()

        # Add new reaction (like or dislike)
        Like.objects.create(user=user, post=post, is_liked=is_liked)

        return JsonResponse({
            "status": "liked" if is_liked else "disliked",
            "likes_count": get_likes(post_id),
            "dislikes_count": get_dislikes(post_id)
        })

    elif request.method == "DELETE":
        # Remove user reaction
        print("Removing like/dislike",is_liked)
        Like.objects.filter(user=user, post=post, is_liked=is_liked).delete()

        return JsonResponse({
            "status": "unliked" if is_liked else "undisliked",
            "likes_count": get_likes(post_id),
            "dislikes_count": get_dislikes(post_id)
        })

def get_likes(post_id):
    return Like.objects.filter(post_id=post_id, is_liked=True).count()

def get_dislikes(post_id):
    return Like.objects.filter(post_id=post_id, is_liked=False).count()

def is_liked_by_user(post_id, user_id):
    return Like.objects.filter(post_id=post_id, user_id=user_id, is_liked=True).exists()

def is_disliked_by_user(post_id, user_id):
    return Like.objects.filter(post_id=post_id, user_id=user_id, is_liked=False).exists()

def get_likes_details(post_id,user_id):
    likes_count = get_likes(post_id)
    dislikes_count = get_dislikes(post_id)
    is_liked = is_liked_by_user(post_id, user_id)
    is_disliked = is_disliked_by_user(post_id, user_id)
    return {"likes_count": likes_count, 
            "dislikes_count": dislikes_count, 
            "is_liked_by_user": is_liked, 
            "is_disliked_by_user": is_disliked}