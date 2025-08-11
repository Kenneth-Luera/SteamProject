from django.db import models
from .UserModels import User
from django.conf import settings
import uuid
from django.db.models import Count
from django.core.exceptions import ValidationError

class ModelBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class CanalMensaje(ModelBase):
    canal = models.ForeignKey('Canal', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()

class CanalUsuario(ModelBase):
    canal = models.ForeignKey('Canal', null=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('canal', 'usuario')
        verbose_name = "Usuario en Canal"
        verbose_name_plural = "Usuarios en Canales"

class CanalQuerySet(models.QuerySet):
    
    def solo_uno(self):
        return self.annotate(num_usuarios= Count('usuarios')).filter(num_usuarios=1)

    def solo_dos(self):
        return self.annotate(num_usuarios= Count('usuarios')).filter(num_usuarios=2)

class CanalManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        return CanalQuerySet(self.model, using=self._db)

class Canal(ModelBase):
    usuarios = models.ManyToManyField(User,blank=True, through=CanalUsuario)

    objects = CanalManager()
    def save(self, *args, **kwargs):
        if self.pk is None and Canal.objects.filter(usuarios=self.usuarios.all()[0]).filter(usuarios=self.usuarios.all()[1]).exists():
            raise ValidationError("Ya existe un canal entre estos usuarios.")
        super().save(*args, **kwargs)