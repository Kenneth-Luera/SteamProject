from .models.UserModels import User
from .models.BibliotecaModels import Biblioteca, JuegoBiblioteca
from .models.GamesModels import Juego
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'fecha_lanzamiento', 'desarrollador']

class BibliotecaSerializer(serializers.ModelSerializer):
    juegos = JuegoSerializer(many=True, read_only=True)

    class Meta:
        model = Biblioteca
        fields = ['id', 'user', 'juegos']

class JuegoBibliotecaSerializer(serializers.ModelSerializer):
    juego = JuegoSerializer(read_only=True)
    biblioteca = BibliotecaSerializer(read_only=True)

    class Meta:
        model = JuegoBiblioteca
        fields = ['id', 'biblioteca', 'juego', 'fecha_adquisicion', 'horas_jugadas', 'ultima_vez_jugado']
        read_only_fields = ['fecha_adquisicion', 'ultima_vez_jugado']