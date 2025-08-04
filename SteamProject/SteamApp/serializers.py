from .models.UserModels import User
from .models.ProfileModels import Profile
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

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'fecha_lanzamiento', 'desarrollador']

class BibliotecaSerializer(serializers.ModelSerializer):
    juegos = Biblioteca

    class Meta:
        model = Biblioteca
        fields = ['id', 'user', 'juegos']

class JuegoBibliotecaSerializer(serializers.ModelSerializer):
    juego = JuegoBiblioteca

    class Meta:
        model = JuegoBiblioteca
        fields = '__all__'
        
class JuegoBibliotecaSerializer(serializers.ModelSerializer):
    juego = JuegoBiblioteca

    class Meta:
        model = JuegoBiblioteca
        fields = 'all'

class BibliotecaSerializer(serializers.ModelSerializer):
    juegos = JuegoBibliotecaSerializer(source='juegobiblioteca_set', many=True)

    class Meta:
        model = Biblioteca
        fields = ['id', 'user', 'juegos']
    