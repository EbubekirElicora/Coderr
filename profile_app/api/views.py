from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from profile_app.models import UserProfile

from .permissions import is_profile_owner
from .serializers import (
    BusinessProfileListSerializer,
    CustomerProfileListSerializer,
    UserProfileSerializer,
)


class ProfileDetailView(APIView):
    """Retrieve or update a user profile."""

    def get_profile(self, pk):
        """Return profile by user id or raise 404."""
        return get_object_or_404(UserProfile, user_id=pk)

    def get(self, request, pk):
        """Return profile details."""
        profile = self.get_profile(pk)
        serializer = UserProfileSerializer(
            profile,
            context={"request": request},
        )

        return Response(serializer.data)

    def patch(self, request, pk):
        """Update the authenticated user's own profile."""
        profile = self.get_profile(pk)

        if not is_profile_owner(request.user, profile):
            raise PermissionDenied("You can only edit your own profile.")

        serializer = UserProfileSerializer(
            profile,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class BusinessProfileListView(APIView):
    """Return all business profiles."""

    def get(self, request):
        """Return a list of business users."""
        profiles = UserProfile.objects.filter(type=UserProfile.BUSINESS)
        serializer = BusinessProfileListSerializer(
            profiles,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


class CustomerProfileListView(APIView):
    """Return all customer profiles."""

    def get(self, request):
        """Return a list of customer users."""
        profiles = UserProfile.objects.filter(type=UserProfile.CUSTOMER)
        serializer = CustomerProfileListSerializer(
            profiles,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)