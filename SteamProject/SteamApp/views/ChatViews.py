from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers import CanalSerializer, CanalMensajeSerializer, CanalUsuarioSerializer
from ..models.ChatModels import Canal, CanalMensaje, CanalUsuario
from ..models.UserModels import User
from django.http import HttpResponse

class MensajesViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, pk):
        try:
            usuario = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        canal = Canal.objects.filter(usuarios=request.user).filter(usuarios=usuario).first()

        
        mensajes = CanalMensaje.objects.filter(canal=canal).order_by('time')
        serializer = CanalMensajeSerializer(mensajes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, pk):
        try:
            usuario = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        canal = Canal.objects.filter(usuarios=request.user).filter(usuarios=usuario).first()

        
        serializer = CanalMensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(canal=canal, usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

