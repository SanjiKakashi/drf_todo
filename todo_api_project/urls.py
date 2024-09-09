from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo-api/", include("todoapp.urls")),
    path("auth/", include("accounts.urls")),
]
