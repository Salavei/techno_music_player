from rest_framework.serializers import ModelSerializer
from ..models import Song


class SongSerializers(ModelSerializer):
    class Meta:
        model = Song
        exclude = ('id', )
