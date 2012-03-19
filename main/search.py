from haystack.indexes import *
from haystack import site
from main.models import *


class ArtistIndex(SearchIndex):
    t = CharField(document=True, model_attr='artist')

    def get_model(self):
        return Artist


class AlbumIndex(SearchIndex):
    t = CharField(document=True, model_attr='album')

    def get_model(self):
        return Album


class SongIndex(SearchIndex):
    t = CharField(document=True, model_attr='song')
    lyrics = CharField(model_attr='lyrics')

    def get_model(self):
        return Song

#site.register(Artist, ArtistIndex)
#site.register(Album, AlbumIndex)
#site.register(Song, SongIndex)

