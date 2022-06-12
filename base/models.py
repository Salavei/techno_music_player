from django.db import models


class Song(models.Model):
    name = models.TextField()
    artist = models.TextField()
    image = models.ImageField()
    path = models.TextField()

    def __str__(self):
        return self.name
