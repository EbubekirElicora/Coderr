from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for user profiles."""

    list_display = [
        "id",
        "user",
        "type",
        "location",
        "tel",
        "created_at",
    ]
    list_filter = [
        "type",
        "created_at",
    ]
    search_fields = [
        "user__username",
        "user__email",
        "location",
        "tel",
    ]