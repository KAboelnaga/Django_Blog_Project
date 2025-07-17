from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('forbidden-words/', views.forbidden_words_list, name='forbidden_words_list'),
    path('forbidden-words/add/', views.add_forbidden_word, name='add_forbidden_word'),
    path('forbidden-words/delete/<int:word_id>/', views.delete_forbidden_word, name='delete_forbidden_word'),
]
