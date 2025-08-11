from .models.UserModels import User
from .models.ProfileModels import *
from .models.BibliotecaModels import Biblioteca, JuegoBiblioteca
from .models.GamesModels import Juego
from .models.ChatModels import Canal, CanalUsuario, CanalMensaje
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
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
<<<<<<< HEAD

class CanalMensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanalMensaje
        fields = ['id', 'canal', 'usuario', 'texto', 'time', 'updated']

class CanalUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanalUsuario
        fields = ['id', 'canal', 'usuario', 'time', 'updated']

class CanalSerializer(serializers.ModelSerializer):
    usuarios = CanalUsuarioSerializer(many=True, read_only=True)

    class Meta:
        model = Canal
        fields = ['id', 'usuarios', 'time', 'updated']
        read_only_fields = ['id', 'time', 'updated']

class MeSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'profile']
        read_only_fields = ['user', 'profile']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if not username or not password:
            raise serializers.ValidationError("Debe enviar username y contraseña")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Contraseña incorrecta")

        # ✅ Creamos el token manualmente (ya no usamos super().validate)
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username,
            'rol': user.rol,
            'user_id': user.id
        }

    # 👇 Este método debe estar dentro de la clase (¡así sí funciona!)
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['user_id'] = user.id
        return token
=======
        
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
    
>>>>>>> 590276fdd5c9dcd8db6128b4e4b1a007e72dd854
