from django.shortcuts import get_object_or_404, render, redirect
from .models import Post ,Category, User
from .forms import PostForm, CategoryForm
from django.contrib import messages
from django.contrib.auth import get_user_model



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

