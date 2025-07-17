from blogs.models import Category
from .models import Subscription

def user_subscriptions(request):
    if request.user.is_authenticated:
        subscriptions = Subscription.objects.filter(user=request.user).values_list('category_id', flat=True)
        categories = Category.objects.all()
        return {'user_subscriptions': list(subscriptions), 'categories': categories}
    return {'user_subscriptions': [], 'categories': Category.objects.all()} 