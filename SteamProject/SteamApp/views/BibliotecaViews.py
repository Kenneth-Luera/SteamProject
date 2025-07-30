from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers import  JuegoBibliotecaSerializer
from ..models.BibliotecaModels import Biblioteca, JuegoBiblioteca
from ..models.GamesModels import Juego

class JuegosBibliotecaViewSet(viewsets.ModelViewSet):
    serializer_class = JuegoBibliotecaSerializer
    queryset = JuegoBiblioteca.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get']


class JuegosBibliotecaPostViewSet(viewsets.ModelViewSet):
    serializer_class = JuegoBibliotecaSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = request.user.id
        saldo = request.user.saldo



        juego_id = request.data.get('juego')
        if not juego_id:
            return Response({"error": "Se requiere el ID del juego"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            juego = Juego.objects.get(id=juego_id)
        except Juego.DoesNotExist:
            return Response({"error": "El juego no existe"}, status=status.HTTP_404_NOT_FOUND)

        game_price = float(juego.precio)



        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.rol == "ADMIN":
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif user:
                if saldo >= game_price:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    request.user.saldo -= game_price
                    request.user.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "que quieres oe pobre."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "No tienes permiso para agregar juegos a esta biblioteca."}, status=status.HTTP_403_FORBIDDEN)
            
        else:
            return Response({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)