from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.serializers.login_serializer import LoginSerializer
from apps.accounts.serializers.register_serializer import RegisterSerializer
from apps.accounts.services.auth_service import generate_tokens


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "message": "User registered successfully.",
                "user": {
                    "email": user.email,
                },
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            if "non_field_errors" in serializer.errors:
                return Response(
                    {"detail": "Invalid email or password."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.validated_data["user"]
        tokens = generate_tokens(user)

        return Response(
            tokens,
            status=status.HTTP_200_OK,
        )
