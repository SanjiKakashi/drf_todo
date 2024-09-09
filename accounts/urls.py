from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import LoginView, SignUpView, getUserList

urlpatterns = [
    path("users", getUserList, name="List of Users"),
    path("signup", SignUpView.as_view(), name="Sign up "),
    path("login", LoginView.as_view(), name="Login"),
    path("jwt/create", TokenObtainPairView.as_view(), name="Token Creation"),
]
