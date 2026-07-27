from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.managers import UserManager
from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):
    """
    Custom User model.
    """

    email = models.EmailField(
        unique=True,
        db_index=True,
    )

    username = models.CharField(
        max_length=150,
        unique=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        db_table = "users"
        ordering = ["-created_at"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email