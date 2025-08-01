from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.URLField(default="https://vanacco.com/wp-content/uploads/2022/01/Videogame-claves-1-1200x1200.jpg")
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    desarrollador = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre