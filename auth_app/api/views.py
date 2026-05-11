from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, RegistrationSerializer


def get_auth_response(user):
    """Return token and user data for authentication endpoints."""
    token, created = Token.objects.get_or_create(user=user)

    return {
        "token": token.key,
        "username": user.username,
        "email": user.email,
        "user_id": user.id,
    }


class RegistrationView(APIView):
    """Create a new user account."""

    permission_classes = [AllowAny]

    def post(self, request):
        """Register a new user and return authentication data."""
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(get_auth_response(user), status=201)


class LoginView(APIView):
    """Authenticate a user and return token data."""

    permission_classes = [AllowAny]

    def post(self, request):
        """Login a user and return authentication data."""
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(get_auth_response(serializer.validated_data["user"]))