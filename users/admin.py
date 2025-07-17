from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.action(description='Promote selected users to Admin')
def promote_to_admin(modeladmin, request, queryset):
    queryset.update(is_admin=True, is_staff=True)

@admin.action(description='Block selected users')
def block_users(modeladmin, request, queryset):
    queryset.update(is_blocked=True)

@admin.action(description='Unblock selected users')
def unblock_users(modeladmin, request, queryset):
    queryset.update(is_blocked=False)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "is_admin", "is_blocked", "is_staff", "is_superuser")
    list_filter = ("is_admin", "is_blocked", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("-created_at",)

    actions = [promote_to_admin, block_users, unblock_users]

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_admin", "is_blocked", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "created_at")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_admin", "is_blocked"),
        }),
    )
