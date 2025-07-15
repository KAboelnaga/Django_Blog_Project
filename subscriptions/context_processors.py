from .models import Subscription

def user_subscriptions(request):
    if request.user.is_authenticated:
        subscriptions = Subscription.objects.filter(user=request.user).values_list('category_id', flat=True)
        return {'user_subscriptions': list(subscriptions)}
    return {'user_subscriptions': []} 