from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taskName = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    taskCreatedAt = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=15)
    taskStatus = models.CharField(max_length=30, blank=True)
    dueDate = models.DateTimeField(default=datetime.now)

    def _str_(self):
        return self.taskName
