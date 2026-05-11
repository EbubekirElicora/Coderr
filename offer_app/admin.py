from django.contrib import admin

from .models import Offer, OfferDetail


class OfferDetailInline(admin.TabularInline):
    """Inline admin configuration for offer details."""

    model = OfferDetail
    extra = 0


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    """Admin configuration for offers."""

    list_display = [
        "id",
        "title",
        "user",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "title",
        "description",
        "user__username",
        "user__email",
    ]
    inlines = [
        OfferDetailInline,
    ]


@admin.register(OfferDetail)
class OfferDetailAdmin(admin.ModelAdmin):
    """Admin configuration for offer details."""

    list_display = [
        "id",
        "offer",
        "offer_type",
        "title",
        "price",
        "delivery_time_in_days",
        "revisions",
    ]
    list_filter = [
        "offer_type",
    ]
    search_fields = [
        "title",
        "offer__title",
    ]