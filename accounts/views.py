from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer
from .tokens import create_jwt_token

# Create your views here.

User = get_user_model()


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data={
                    "message": "User Created Successfully",
                    "payload": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    # @staticmethod
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            return Response(
                data={"message": "Email is Not registerd"},
                status=status.HTTP_404_NOT_FOUND,
            )
        user = authenticate(email=email, password=password)

        if user is not None:
            token = create_jwt_token(user)
            return Response(
                data={
                    "message": "User Logged in Successfully",
                    "tokens": token,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(data={"error": "Invalid email or password"})

    @staticmethod
    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([])
def getUserList(request: Request):
    users = User.objects.all()
    if not users.exists():
        return Response(
            data={"message": "No User is Registered"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = SignUpSerializer(users, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
