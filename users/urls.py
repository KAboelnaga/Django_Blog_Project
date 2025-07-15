from django.urls import path
from . import views
urlpatterns = [

    path('', views.users_list, name='users_list'),
    path('create/', views.create_user_view, name='create_user'),
    path('<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('<int:user_id>/promote/', views.promote_user_view, name='promote_user'),

]