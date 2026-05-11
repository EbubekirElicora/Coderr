from django.contrib.auth.models import User
from rest_framework import serializers

from profile_app.models import UserProfile
from review_app.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for review responses."""

    class Meta:
        model = Review
        fields = [
            "id",
            "business_user",
            "reviewer",
            "rating",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "reviewer",
            "created_at",
            "updated_at",
        ]


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating reviews."""

    class Meta:
        model = Review
        fields = [
            "business_user",
            "rating",
            "description",
        ]

    def validate_business_user(self, value):
        """Validate that the reviewed user is a business user."""
        if not hasattr(value, "profile"):
            raise serializers.ValidationError("User has no profile.")

        if value.profile.type != UserProfile.BUSINESS:
            raise serializers.ValidationError(
                "Reviews can only be created for business users."
            )

        return value

    def validate_rating(self, value):
        """Validate rating range."""
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )

        return value

    def validate(self, attrs):
        """Validate unique review per business user."""
        request = self.context["request"]
        business_user = attrs["business_user"]

        review_exists = Review.objects.filter(
            business_user=business_user,
            reviewer=request.user,
        ).exists()

        if review_exists:
            raise serializers.ValidationError(
                "You already reviewed this business user."
            )

        return attrs

    def create(self, validated_data):
        """Create a review for the current customer."""
        request = self.context["request"]

        return Review.objects.create(
            reviewer=request.user,
            **validated_data,
        )

    def to_representation(self, instance):
        """Return full review data after creation."""
        return ReviewSerializer(instance).data


class ReviewUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating reviews."""

    class Meta:
        model = Review
        fields = [
            "rating",
            "description",
        ]

    def validate_rating(self, value):
        """Validate rating range."""
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )

        return value

    def to_representation(self, instance):
        """Return full review data after update."""
        return ReviewSerializer(instance).data