from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.UserModels import User
from .models.ProfileModels import Profile
from .models.BibliotecaModels import Biblioteca

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Biblioteca.objects.create(user=instance)