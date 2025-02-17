from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def create_jwt_token(user):
    refresh = RefreshToken.for_user(user)

    tokens = {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
    }
    return tokens
