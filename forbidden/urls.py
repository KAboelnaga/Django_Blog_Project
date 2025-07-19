from django.urls import path
from . import views

app_name = 'forbidden'
urlpatterns = [
    path('', views.forbidden_words_list, name='forbidden_words_list'),
    path('add/', views.add_forbidden_word, name='add_forbidden_word'),
    path('edit/<int:pk>/', views.edit_forbidden_word, name='edit_forbidden_word'),
    path('delete/<int:pk>/', views.delete_forbidden_word, name='delete_forbidden_word'),
    
]
