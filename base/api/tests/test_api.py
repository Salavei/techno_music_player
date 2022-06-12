from rest_framework.test import APITestCase
from ...models import Song
from django.urls import reverse
from ..serializers import SongSerializers
from rest_framework.status import HTTP_200_OK


class SongApiTestCase(APITestCase):
    def test_get(self):
        song_1 = Song.objects.create(name='HRA PODCAST', artist='TECHNOKOOL',
                                     path='hraberlin/hra-podcast-63-technokool?in=technokoolmusic/sets/podcasts')
        song_2 = Song.objects.create(name='Bassiani invites', artist='SPFDJ',
                                     path='bassiani/bassiani-invites-spfdj-podcast-109')
        url = reverse('song-list')
        response = self.client.get(url)
        serializer_data = SongSerializers([song_1, song_2], many=True).data
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

