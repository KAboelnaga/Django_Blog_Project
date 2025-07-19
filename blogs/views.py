import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Like, Tags
from comments.forms import CommentForm
from comments.models import Comment
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .forms import PostForm, CategoryForm, TagsForm
from django.contrib import messages
from django.contrib.auth import get_user_model

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

def home(request):
    tag_query = request.GET.get('tag')

    posts = Post.objects.order_by('-created_at')
    if tag_query:
        posts = posts.filter(tags__name__icontains=tag_query).distinct()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    tags = Tags.objects.all()

    return render(request, 'blogs/home.html', {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags,
        'tag_query': tag_query,
    })


def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tag_query = request.GET.get('tag')
    posts = Post.objects.filter(category=category).order_by('-created_at')
    if tag_query:
        posts = posts.filter(tags__name__icontains=tag_query).distinct()
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

def create_tag(request):
    form = TagsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tag created successfully!')
        return redirect('blogs:tags_list')

    return render(request, 'blogs/tag_create.html', {'form': form})

def tags_list(request):
    tags = Tags.objects.all()
    return render(request, 'blogs/tags_list.html', {'tags': tags})

def tag_update(request, pk):
    tag = get_object_or_404(Tags, pk=pk)
    form = TagsForm(request.POST or None, instance=tag)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tag updated successfully!')
        return redirect('blogs:tags_list')
    return render(request, 'blogs/tag_form.html', {'form': form})
def tag_delete(request, pk):
    tag = get_object_or_404(Tags, pk=pk)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, 'Tag deleted successfully!')
        return redirect('blogs:tags_list')
    return render(request, 'blogs/tag_confirm_delete.html', {'tag': tag})
def create_post(request):
    post_form = PostForm()
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.save()  # Save post first to assign tags

            # Process custom tags input
            tags_data = post_form.cleaned_data.get('tags_input')
            if tags_data:
                tags = [tag.strip() for tag in tags_data.split(',') if tag.strip()]
                tag_objs = [Tags.objects.get_or_create(name=tag)[0] for tag in tags]
                post.tags.set(tag_objs)
            else:
                post.tags.clear()

            messages.success(request, 'Post created successfully!')
            return redirect('blogs:posts_list')

    return render(request, 'blogs/post_create.html', {'form': post_form})




def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        tags_data = form.cleaned_data.get('tags_input')
        if tags_data:
            tags = [tag.strip() for tag in tags_data.split(',') if tag.strip()]
            tag_objs = [Tags.objects.get_or_create(name=tag)[0] for tag in tags]
            post.tags.set(tag_objs)
        else:
            post.tags.clear()
        messages.success(request, 'Post updated successfully!')
        return redirect('blogs:posts_list')
    return render(request, 'blogs/post_edit.html', {'form': form})


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