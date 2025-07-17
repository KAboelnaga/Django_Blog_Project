from django.urls import path
from .views import user_register, user_login, user_logout, blocked_page, manage_users, toggle_admin, toggle_block

app_name = 'users'

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('blocked/', blocked_page, name='blocked_page'),
    path("manage-users/", manage_users, name="manage_users"),
    path("toggle-admin/<int:user_id>/", toggle_admin, name="toggle_admin"),
    path("toggle-block/<int:user_id>/", toggle_block, name="toggle_block"),
]