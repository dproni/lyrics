# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

# -*- coding: utf-8 -*-

from scrapy.contrib_exp.djangoitem import DjangoItem
from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose
from main.models import *

class LyricsItem(Item):
    #A_artists = Field(input_processor=MapCompose(lambda s: s.replace('&amp;', '&')))
    artist_name = Field(output_processor=MapCompose(lambda s: s.replace('&amp;', '&').encode('utf-8')))
    song_name = Field(output_processor=MapCompose(lambda s: s.encode('utf-8')))
    text = Field(output_processor=MapCompose(lambda s: s.encode('utf-8')))


class ArtistParsed(DjangoItem):
    django_model = Artist

#    artist_name = Artist.artist