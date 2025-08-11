from django.contrib import admin

# Register your models here.

from .models.UserModels import User
from .models.ProfileModels import Profile
from .models.GamesModels import Juego
from .models.BibliotecaModels import Biblioteca, JuegoBiblioteca
from .models.ChatModels import Canal, CanalUsuario, CanalMensaje

class CanalMensajeInline(admin.TabularInline):
    model = CanalMensaje
    extra = 1

class CanalUsuarioInline(admin.TabularInline):
    model = CanalUsuario
    extra = 1

class CanalAdmin(admin.ModelAdmin):
    inlines = [CanalUsuarioInline, CanalMensajeInline]

    class Meta:
        model = Canal

admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalUsuario)
admin.site.register(CanalMensaje)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Juego)
admin.site.register(Biblioteca)
admin.site.register(JuegoBiblioteca)
