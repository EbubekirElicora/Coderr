from django.db.models import Avg
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from offer_app.models import Offer
from profile_app.models import UserProfile
from review_app.models import Review


class BaseInfoView(APIView):
    """Return general marketplace statistics."""

    permission_classes = [AllowAny]

    def get(self, request):
        """Return review, rating, profile and offer statistics."""
        average_rating = Review.objects.aggregate(
            average=Avg("rating")
        )["average"]

        data = {
            "review_count": Review.objects.count(),
            "average_rating": round(average_rating or 0, 1),
            "business_profile_count": UserProfile.objects.filter(
                type=UserProfile.BUSINESS,
            ).count(),
            "offer_count": Offer.objects.count(),
        }

        return Response(data)