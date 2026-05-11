from rest_framework import serializers

from offer_app.models import OfferDetail
from order_app.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for order responses."""

    price = serializers.IntegerField()

    class Meta:
        model = Order
        fields = [
            "id",
            "customer_user",
            "business_user",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
            "offer_type",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields


class OrderCreateSerializer(serializers.Serializer):
    """Serializer for creating orders from offer details."""

    offer_detail_id = serializers.IntegerField(write_only=True)

    def validate_offer_detail_id(self, value):
        """Validate that the offer detail exists."""
        try:
            self.offer_detail = OfferDetail.objects.select_related(
                "offer",
                "offer__user",
            ).get(pk=value)
        except OfferDetail.DoesNotExist as exc:
            raise serializers.ValidationError(
                "Offer detail does not exist."
            ) from exc

        return value

    def create(self, validated_data):
        """Create an order from the selected offer detail."""
        request = self.context["request"]
        offer_detail = self.offer_detail

        return Order.objects.create(
            customer_user=request.user,
            business_user=offer_detail.offer.user,
            title=offer_detail.title,
            revisions=offer_detail.revisions,
            delivery_time_in_days=offer_detail.delivery_time_in_days,
            price=offer_detail.price,
            features=offer_detail.features,
            offer_type=offer_detail.offer_type,
        )

    def to_representation(self, instance):
        """Return full order data after creation."""
        return OrderSerializer(instance).data


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating an order status."""

    class Meta:
        model = Order
        fields = [
            "status",
        ]