from django.urls import include, path

from .views import TodoDelete, TodoListAndCreate

urlpatterns = [
    path("list", TodoListAndCreate.as_view(), name="List of Task"),
    path("<int:pk>/delete", TodoDelete.as_view(), name="Delete a Task"),
    # path("create-task", createATask, name="Create Task"),
    # path("delete-task/<int:index>", deleteTask, name="Delete Task"),
    # path("update-task/<int:index>", updateTask, name="Update Task"),
    # path(
    #     "update-delete/<int:pk>",
    #     TodoUpdateReteriveDelete.as_view(),
    #     name="Update and Delete Task",
    # ),
]
