from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
