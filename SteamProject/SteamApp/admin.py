from django.contrib import admin

# Register your models here.

from .models.UserModels import User
from .models.ProfileModels import Profile
from .models.GamesModels import Juego
from .models.BibliotecaModels import Biblioteca, JuegoBiblioteca

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Juego)
admin.site.register(Biblioteca)
admin.site.register(JuegoBiblioteca)
