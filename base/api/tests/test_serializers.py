from django.test import TestCase
from ...models import Song
from ..serializers import SongSerializers


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        song_1 = Song.objects.create(name='HRA PODCAST', artist='TECHNOKOOL',
                                     path='hraberlin/hra-podcast-63-technokool?in=technokoolmusic/sets/podcasts')
        song_2 = Song.objects.create(name='Bassiani invites', artist='SPFDJ',
                                     path='bassiani/bassiani-invites-spfdj-podcast-109')
        
        data = SongSerializers([song_1, song_2], many=True).data
        expected_data = [
            {
                'name': 'HRA PODCAST',
                'artist': 'TECHNOKOOL',
                'image': None,
                'path': 'hraberlin/hra-podcast-63-technokool?in=technokoolmusic/sets/podcasts'
            },
            {
                'name': 'Bassiani invites',
                'artist': 'SPFDJ',
                'image': None,
                'path': 'bassiani/bassiani-invites-spfdj-podcast-109'
            },
        ]
        self.assertEqual(expected_data, data)
