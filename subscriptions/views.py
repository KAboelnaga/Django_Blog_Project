from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from blogs.models import Category
from .models import Subscription
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

@login_required
def subscribe(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    try:
        Subscription.objects.create(user=request.user, category=category)
        messages.success(request, f'You have successfully subscribed to {category.name}.')
        
        # Send confirmation email
        subject = 'Subscription Confirmation'
        message = f'Hi {request.user.username},\n\nYou have successfully subscribed to the category: {category.name}.\n\nThank you for subscribing!'
        from_email = settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'webmaster@localhost'
        to_email = [request.user.email]
        
        send_mail(subject, message, from_email, to_email, fail_silently=False)

    except IntegrityError:
        messages.warning(request, f'You are already subscribed to {category.name}.')
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def unsubscribe(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subscription = Subscription.objects.filter(user=request.user, category=category)
    if subscription.exists():
        subscription.delete()
        messages.success(request, f'You have successfully unsubscribed from {category.name}.')
    else:
        messages.warning(request, f'You were not subscribed to {category.name}.')
    return redirect(request.META.get('HTTP_REFERER', '/'))
