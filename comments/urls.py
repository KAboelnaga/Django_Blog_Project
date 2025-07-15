from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('', views.add_comment, name='add_comment'),
    path('<int:parent_id>/', views.add_comment, name='reply_comment'),

]