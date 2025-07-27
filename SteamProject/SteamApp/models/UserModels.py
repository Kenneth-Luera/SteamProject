from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    ROL_CHOICES = (
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
        ('MODERATOR', 'Moderator'),
        ('DEV','Creador de juegos')
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='USER')
    ESTADO_CHOICES = (
        ('ACTIVE', 'Active'),
        ('SUSPENDIDO', 'Suspended'),
        ('BANNED', 'Banned')
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='USER')
    date_joined = models.DateTimeField(default=now)

    def __str__(self):
        return self.username

