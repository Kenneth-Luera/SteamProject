from ..serializers import ProfileSerializer
from ..models.ProfileModels import Profile
from rest_framework import viewsets

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()