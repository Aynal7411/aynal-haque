from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .models import Profile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom User Admin configuration.
    """

    ordering = ["-created_at"]

    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "created_at",
    ]

    list_filter = [
        "is_active",
        "is_staff",
        "is_superuser",
        "created_at",
    ]

    search_fields = [
        "email",
        "username",
        "first_name",
        "last_name",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
        "last_login",
        "date_joined",
    ]

    fieldsets = (
        (
            "Account Information",
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                )
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "Create User",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "location",
        "created_at",
    ]

    search_fields = [
        "user__email",
        "location",
    ]