from django.db import models
from .UserModels import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="User")
    nickname = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    avatar = models.URLField(default="https://i.pinimg.com/236x/d4/74/1c/d4741cb779ddec6509ca1ae0cb137a7d.jpg")
    frame = models.URLField(default="https://cdn.fastly.steamstatic.com/steamcommunity/public/images/items/860950/6e1b5f5977036a189465f5455f2c54722c12883d.png")
    background = models.URLField(default="https://w.wallhaven.cc/full/9o/wallhaven-9o687w.png")

    '''
    - Comentarios
    - Insgnias
    '''

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
class Me (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Me")
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="MeProfile")

    def __str__(self):
        return f"Me de {self.user.username}"
    
    class Meta:
        verbose_name = "Me"
        verbose_name_plural = "Mes"

