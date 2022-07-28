from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(db_index=True, max_length=100, unique=True)
    email = models.EmailField(db_index=True, max_length=100, unique=True)
    password = models.CharField(max_length=255)
    vote_for = models.IntegerField(null=True, default=None)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
