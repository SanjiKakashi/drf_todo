from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoModel
from .serializers import ToDoSerializers, serializers


class TodoListAndCreate(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = ToDoSerializers
    queryset = TodoModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data={
                        "message": "Task is created successfully",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except TypeError as te:
            return Response(
                data={"error": str(te)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(data=type(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TodoDelete(generics.GenericAPIView, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer = ToDoSerializers
    queryset = TodoModel.objects.all()

    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TodoUpdateReteriveDelete(
    generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    serializer_class = ToDoSerializers
    queryset = TodoModel.objects.all()

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
