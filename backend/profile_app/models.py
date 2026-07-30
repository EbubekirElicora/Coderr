from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    """Represents additional profile data for a customer or business user."""

    CUSTOMER = "customer"
    BUSINESS = "business"

    USER_TYPE_CHOICES = [
        (CUSTOMER, "Customer"),
        (BUSINESS, "Business"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
    )
    file = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )
    tel = models.CharField(
        max_length=50,
        blank=True,
        default="",
    )
    description = models.TextField(
        blank=True,
        default="",
    )
    working_hours = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"
        ordering = ["user__username"]

    def __str__(self):
        return f"{self.user.username} ({self.type})"