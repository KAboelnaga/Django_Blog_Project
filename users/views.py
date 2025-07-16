from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, LoginForm
# Create your views here.

def user_register (request):
    if request.user.is_authenticated:
        return redirect('blogs:home')
    
    if request.method == 'POST':
        register_form = UserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registration successful! Please log in.')
    else:
        register_form = UserForm()
    context = {'register_form': register_form}
    return render(request, 'users/register.html', context)

def user_login (request):

    if request.user.is_authenticated:
        return redirect('blogs:home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_active:
                messages.error(request,"Sorry, you are blocked. Contact the admin.")
                logout(request)
                return redirect('blog_auth:login')
            
            login(request, user)

            if request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            
            return redirect('blogs:home')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('users:login')

def blocked_page(request):
    return render(request, 'users/blocked.html')


def is_superadmin(user):
    return user.is_authenticated and (user.is_superuser or user.is_admin)

@user_passes_test(is_superadmin)
def manage_users(request):
    users = User.objects.exclude(pk=request.user.pk)
    return render(request, "users/manage_users.html", {"users": users})

@login_required
@user_passes_test(is_superadmin)
def toggle_admin(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_admin = not user.is_admin
    user.save()
    return redirect("users:manage_users")

@login_required
@user_passes_test(is_superadmin)
def toggle_block(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_blocked = not user.is_blocked
    user.save()
    return redirect("users:manage_users")
