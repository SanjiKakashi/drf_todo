from enum import unique

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("User is Not the Staff")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("User is not a Super User")

        super_user = self.create_user(email=email, password=password, **extra_fields)
        return super_user


class User(AbstractUser):

    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(
        max_length=50,
    )
    date_of_birth = models.DateField(null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()

    def __str__(self):
        return self.email
