from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    
    def __str__(self) -> str:
        return f"{self.username} {self.first_name}"