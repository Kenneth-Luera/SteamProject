from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.timezone import now

class User(AbstractBaseUser):
    nickname = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    ROL_CHOICES = (
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
        ('MODERATOR', 'Moderator'),
        ('DEV','Creador de juegos')
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='USER')
    email = models.EmailField(max_length=254, unique=True)
    ESTADO_CHOICES = (
        ('ACTIVE', 'Active'),
        ('SUSPENDIDO', 'Suspended'),
        ('BANNED', 'Banned')
    )
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='ACTIVE')

    def __str__(self):
        return f"{self.nickname} ({self.id})"