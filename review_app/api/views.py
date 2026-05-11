from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from review_app.models import Review

from .permissions import is_customer_user, is_review_owner
from .serializers import (
    ReviewCreateSerializer,
    ReviewSerializer,
    ReviewUpdateSerializer,
)


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for review endpoints."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    def get_queryset(self):
        """Return filtered and ordered reviews."""
        queryset = self.queryset
        queryset = self.filter_queryset_by_params(queryset)

        return self.order_queryset(queryset)

    def get_serializer_class(self):
        """Return serializer class based on the action."""
        if self.action == "create":
            return ReviewCreateSerializer

        if self.action == "partial_update":
            return ReviewUpdateSerializer

        return ReviewSerializer

    def create(self, request):
        """Create a review as customer user."""
        if not is_customer_user(request.user):
            raise PermissionDenied("Only customer users can create reviews.")

        serializer = self.get_serializer(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def partial_update(self, request, pk=None):
        """Update a review owned by the current user."""
        review = self.get_object()

        if not is_review_owner(request.user, review):
            raise PermissionDenied("Only the creator can edit this review.")

        serializer = self.get_serializer(
            review,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Delete a review owned by the current user."""
        review = self.get_object()

        if not is_review_owner(request.user, review):
            raise PermissionDenied("Only the creator can delete this review.")

        review.delete()
        return Response(status=204)

    def filter_queryset_by_params(self, queryset):
        """Apply review query parameter filters."""
        business_user_id = self.request.query_params.get("business_user_id")
        reviewer_id = self.request.query_params.get("reviewer_id")

        if business_user_id:
            queryset = queryset.filter(business_user_id=business_user_id)

        if reviewer_id:
            queryset = queryset.filter(reviewer_id=reviewer_id)

        return queryset

    def order_queryset(self, queryset):
        """Apply allowed ordering."""
        ordering = self.request.query_params.get("ordering")

        if ordering in ["updated_at", "-updated_at", "rating", "-rating"]:
            return queryset.order_by(ordering)

        return queryset.order_by("-updated_at")