from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, User
from comments.forms import CommentForm
from comments.models import Comment
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .forms import PostForm, CategoryForm
from django.contrib import messages
from django.contrib.auth import get_user_model

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
   




def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blogs/posts_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts_list') 
    else:
        form = PostForm()
    return render(request, 'blogs/post_create.html', {'form': form})
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/post_create.html', {'form': form})
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')
    return render(request, 'blogs/post_confirm_delete.html', {'post': post})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blogs/categories_list.html', {'categories': categories})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categories_list')
    return render(request, 'blogs/category_form.html', {'form': form})


def category_update(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        return redirect('categories_list')
    return render(request, 'blogs/category_form.html', {'form': form})


def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect('categories_list')
    return render(request, 'blogs/category_confirm_delete.html', {'cat': cat})

