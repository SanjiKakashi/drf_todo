from django.contrib import admin

from .models import TodoModel

# Register your models here.


@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):

    list_display = ["taskName", "description", "taskCreatedAt"]
    list_filter = ["taskCreatedAt"]
