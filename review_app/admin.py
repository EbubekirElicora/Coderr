from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin configuration for reviews."""

    list_display = [
        "id",
        "business_user",
        "reviewer",
        "rating",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "rating",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "business_user__username",
        "business_user__email",
        "reviewer__username",
        "reviewer__email",
        "description",
    ]