from django.db.models import Min, Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from offer_app.models import Offer, OfferDetail

from .permissions import is_business_user, is_offer_owner
from .serializers import (
    OfferDetailReadSerializer,
    OfferDetailSerializer,
    OfferListSerializer,
    OfferWriteSerializer,
)


class OfferViewSet(viewsets.ModelViewSet):
    """ViewSet for offer CRUD endpoints."""

    queryset = Offer.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    def get_permissions(self):
        """Return permissions based on the action."""
        if self.action == "list":
            return [AllowAny()]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        """Return filtered, searched and ordered offers."""
        queryset = self.queryset.annotate(
            min_price_value=Min("details__price"),
            min_delivery_time_value=Min("details__delivery_time_in_days"),
        )
        queryset = self.filter_queryset_by_params(queryset)
        queryset = self.search_queryset(queryset)

        return self.order_queryset(queryset)

    def get_serializer_class(self):
        """Return serializer class based on the action."""
        if self.action == "list":
            return OfferListSerializer

        if self.action in ["create", "partial_update"]:
            return OfferWriteSerializer

        return OfferDetailReadSerializer

    def create(self, request):
        """Create a new offer as business user."""
        if not is_business_user(request.user):
            raise PermissionDenied("Only business users can create offers.")

        serializer = self.get_serializer(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=201)

    def partial_update(self, request, pk=None):
        """Update an offer owned by the current user."""
        offer = self.get_object()

        if not is_offer_owner(request.user, offer):
            raise PermissionDenied("Only the creator can edit this offer.")

        serializer = self.get_serializer(
            offer,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Delete an offer owned by the current user."""
        offer = self.get_object()

        if not is_offer_owner(request.user, offer):
            raise PermissionDenied("Only the creator can delete this offer.")

        offer.delete()
        return Response(status=204)

    def filter_queryset_by_params(self, queryset):
        """Apply offer query parameter filters."""
        creator_id = self.request.query_params.get("creator_id")
        min_price = self.request.query_params.get("min_price")
        max_delivery_time = self.request.query_params.get("max_delivery_time")

        if creator_id:
            queryset = queryset.filter(user_id=creator_id)

        if min_price:
            queryset = queryset.filter(details__price__gte=min_price)

        if max_delivery_time:
            queryset = queryset.filter(
                details__delivery_time_in_days__lte=max_delivery_time
            )

        return queryset.distinct()

    def search_queryset(self, queryset):
        """Apply title and description search."""
        search = self.request.query_params.get("search")

        if not search:
            return queryset

        return queryset.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )

    def order_queryset(self, queryset):
        """Apply allowed ordering."""
        ordering = self.request.query_params.get("ordering")

        if ordering == "min_price":
            return queryset.order_by("min_price_value")

        if ordering == "-min_price":
            return queryset.order_by("-min_price_value")

        if ordering in ["updated_at", "-updated_at"]:
            return queryset.order_by(ordering)

        return queryset.order_by("-updated_at")


class OfferDetailView(APIView):
    """Retrieve a single offer detail."""

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Return one offer detail."""
        offer_detail = get_object_or_404(OfferDetail, pk=pk)
        serializer = OfferDetailSerializer(offer_detail)

        return Response(serializer.data)