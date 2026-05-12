from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from order_app.models import Order

from .permissions import (
    can_see_order,
    is_business_user,
    is_customer_user,
    is_order_business,
)
from .serializers import (
    OrderCreateSerializer,
    OrderSerializer,
    OrderStatusUpdateSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for order endpoints."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = None
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    def get_queryset(self):
        """Return orders related to the current user or all for admins."""
        user = self.request.user

        if user.is_staff:
            return self.queryset.all()

        return self.queryset.filter(
            customer_user=user
        ) | self.queryset.filter(
            business_user=user
     )
    
    def get_serializer_class(self):
        """Return serializer class based on the action."""
        if self.action == "create":
            return OrderCreateSerializer

        if self.action == "partial_update":
            return OrderStatusUpdateSerializer

        return OrderSerializer

    def create(self, request):
        """Create an order as customer user."""
        if not is_customer_user(request.user):
            raise PermissionDenied("Only customer users can create orders.")

        serializer = self.get_serializer(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        """Return one order if the user is involved."""
        order = self.get_object()

        if not can_see_order(request.user, order):
            raise PermissionDenied("You are not allowed to view this order.")

        serializer = self.get_serializer(order)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """Update order status as related business user."""
        order = self.get_object()

        if not is_order_business(request.user, order):
            raise PermissionDenied("Only the business user can update orders.")

        serializer = self.get_serializer(
            order,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(OrderSerializer(order).data)

    def destroy(self, request, pk=None):
        """Delete an order as admin user."""
        order = self.get_object()

        if not request.user.is_staff:
            raise PermissionDenied("Only admin users can delete orders.")

        order.delete()
        return Response(status=204)


class OrderCountView(APIView):
    """Return active order count for a business user."""

    def get(self, request, business_user_id):
        """Return count of in progress orders."""
        count = Order.objects.filter(
            business_user_id=business_user_id,
            status=Order.IN_PROGRESS,
        ).count()

        return Response({"order_count": count})


class CompletedOrderCountView(APIView):
    """Return completed order count for a business user."""

    def get(self, request, business_user_id):
        """Return count of completed orders."""
        count = Order.objects.filter(
            business_user_id=business_user_id,
            status=Order.COMPLETED,
        ).count()

        return Response({"completed_order_count": count})