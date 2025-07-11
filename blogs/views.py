from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

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

    return render(request, 'blogs/category_posts.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category,
    })
