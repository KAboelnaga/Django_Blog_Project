# subscriptions/urls.py
from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('subscribe/<int:category_id>/', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:category_id>/', views.unsubscribe, name='unsubscribe'),
]
