from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers import UserSerializers
from ..models.UserModels import User

class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]
    http_method_names = ['post']

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get', 'put']

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                queryset = User.objects.all()
            elif request.user.is_superuser == 0:
                return Response({"error": "No tienes permisos para ver la lista de usuarios."}, status=status.Http_403_FORBIDDEN)
        else:
            return Response ({"error": "Usuario no autenticado"},status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)