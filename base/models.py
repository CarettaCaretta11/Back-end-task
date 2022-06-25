from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    completed_quiz = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, default="https://res.cloudinary.com/dn3laf4bh/image/upload/v1647623057/avatar_iu9mmi.svg")
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username