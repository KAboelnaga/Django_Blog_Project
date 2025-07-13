from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from blogs.models import Category
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def subscribe(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    request.user.subscriptions.add(category)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def unsubscribe(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    request.user.subscriptions.remove(category)
    return redirect(request.META.get('HTTP_REFERER', '/'))
