from rest_framework.viewsets import ModelViewSet
from .serializers import SongSerializers
from ..models import Song
from rest_framework import permissions


class SongViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializers
