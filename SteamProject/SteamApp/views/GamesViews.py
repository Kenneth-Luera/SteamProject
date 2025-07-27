from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers import JuegoSerializer
from ..models.GamesModels import Juego

class JuegosViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            juego_id = kwargs.get('pk')
            try:
                juego = Juego.objects.get(id=juego_id)
            except Juego.DoesNotExist:
                return Response({"error": "Juego no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(juego, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            juego_id = kwargs.get('pk')
            try:
                juego = Juego.objects.get(id=juego_id)
                juego.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Juego.DoesNotExist:
                return Response({"error": "Juego no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "No tienes permisos para eliminar juegos."}, status=status.HTTP_403_FORBIDDEN)