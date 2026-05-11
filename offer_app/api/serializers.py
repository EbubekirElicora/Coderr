from django.db.models import Min
from rest_framework import serializers

from offer_app.models import Offer, OfferDetail


def build_offer_detail_url(request, detail):
    """Build absolute URL for an offer detail."""
    path = f"/api/offerdetails/{detail.id}/"

    if request:
        return request.build_absolute_uri(path)

    return path


class OfferDetailShortSerializer(serializers.ModelSerializer):
    """Serializer for short offer detail references."""

    url = serializers.SerializerMethodField()

    class Meta:
        model = OfferDetail
        fields = [
            "id",
            "url",
        ]

    def get_url(self, obj):
        """Return the detail endpoint URL."""
        request = self.context.get("request")
        return build_offer_detail_url(request, obj)


class OfferDetailSerializer(serializers.ModelSerializer):
    """Serializer for full offer detail data."""

    price = serializers.IntegerField()

    class Meta:
        model = OfferDetail
        fields = [
            "id",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
            "offer_type",
        ]


class OfferUserDetailsSerializer(serializers.Serializer):
    """Serializer for offer creator details."""

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()


class OfferListSerializer(serializers.ModelSerializer):
    """Serializer for paginated offer list responses."""

    details = OfferDetailShortSerializer(many=True, read_only=True)
    min_price = serializers.SerializerMethodField()
    min_delivery_time = serializers.SerializerMethodField()
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = [
            "id",
            "user",
            "title",
            "image",
            "description",
            "created_at",
            "updated_at",
            "details",
            "min_price",
            "min_delivery_time",
            "user_details",
        ]

    def get_min_price(self, obj):
        """Return the lowest detail price."""
        price = obj.details.aggregate(min_price=Min("price"))["min_price"]
        return int(price) if price is not None else None

    def get_min_delivery_time(self, obj):
        """Return the shortest delivery time."""
        delivery_time = obj.details.aggregate(
            min_time=Min("delivery_time_in_days")
        )["min_time"]
        return delivery_time

    def get_user_details(self, obj):
        """Return public creator data."""
        return {
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
            "username": obj.user.username,
        }


class OfferDetailReadSerializer(OfferListSerializer):
    """Serializer for one offer with detail URLs."""

    pass


class OfferCreateResponseSerializer(serializers.ModelSerializer):
    """Serializer for offer create and update responses."""

    details = OfferDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Offer
        fields = [
            "id",
            "title",
            "image",
            "description",
            "details",
        ]
        

class OfferWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating offers."""

    details = OfferDetailSerializer(many=True)

    class Meta:
        model = Offer
        fields = [
            "id",
            "title",
            "image",
            "description",
            "details",
        ]
        read_only_fields = [
            "id",
        ]

    def validate_details(self, value):
        """Validate offer detail types."""
        offer_types = [detail["offer_type"] for detail in value]

        if len(offer_types) != len(set(offer_types)):
            raise serializers.ValidationError("Offer types must be unique.")

        return value

    def validate(self, attrs):
        """Validate create and update data."""
        if self.instance is None:
            self.validate_create_details(attrs)

        return attrs

    def validate_create_details(self, attrs):
        """Validate that new offers contain three details."""
        details = attrs.get("details", [])

        if len(details) != 3:
            raise serializers.ValidationError(
                {"details": "An offer must contain exactly three details."}
            )

    def create(self, validated_data):
        """Create an offer with its details."""
        details_data = validated_data.pop("details")
        offer = Offer.objects.create(**validated_data)

        for detail_data in details_data:
            OfferDetail.objects.create(offer=offer, **detail_data)

        return offer

    def update(self, instance, validated_data):
        """Update offer and optionally its details."""
        details_data = validated_data.pop("details", [])
        self.update_offer(instance, validated_data)
        self.update_details(instance, details_data)

        return instance

    def update_offer(self, offer, validated_data):
        """Update basic offer fields."""
        for field, value in validated_data.items():
            setattr(offer, field, value)

        offer.save()

    def update_details(self, offer, details_data):
        """Update offer details by offer type."""
        for detail_data in details_data:
            offer_type = detail_data.get("offer_type")
            detail = offer.details.get(offer_type=offer_type)
            self.update_detail(detail, detail_data)

    def update_detail(self, detail, detail_data):
        """Update one offer detail."""
        for field, value in detail_data.items():
            setattr(detail, field, value)

        detail.save()

    def to_representation(self, instance):
        """Return full offer data after write operations."""
        return OfferCreateResponseSerializer(
            instance,
            context=self.context,
        ).data