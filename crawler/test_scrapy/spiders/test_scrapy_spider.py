# -*- coding: utf-8 -*-

import re

from test_scrapy.items import LyricsItem, ArtistParsed
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Compose
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.selector import HtmlXPathSelector

class LyricsLoader(XPathItemLoader):
    default_input_processor = MapCompose(lambda s: re.sub('\s+', ' ', s.strip()))
    
class LyricsSpider(CrawlSpider):

    name = "test_scrapy"
    allowed_domains = ["lyrcs.ru"]
    start_urls = ["http://lyrcs.ru/letters/X"]

    CLOSESPIDER_ITEMCOUNT = 10

    rules = (
             Rule(SgmlLinkExtractor(allow=('letters/X')), follow=True),
             Rule(SgmlLinkExtractor(allow=('letters/X\?page.+')), follow=True),
             Rule(SgmlLinkExtractor(allow=('artists/.+'),restrict_xpaths=('//div[@id="letter_page"]')), follow=True),
             Rule(SgmlLinkExtractor(allow=('tracks.+'),restrict_xpaths=('//div[@id="artist_page"]')), follow=True, callback='parse_item'),
             #Rule(SgmlLinkExtractor(allow=('letters/A\?page.+')), callback='parse_item'),
            )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        a = ArtistParsed()
#        l = LyricsLoader(LyricsItem(), hxs)
        a['artist'] = 'dsd'
        # l.add_xpath('A_artists', '//div[contains(@id, "col")]/a/text()')
#        l.add_xpath('artist_name', '//div[@id="artist_title"]/span/a/text()')
#        l.add_xpath('song_name', '//div[@id="artist_title"]/h1/text()')
#        l.add_xpath('text', '//div[@id="lyrics"]/div/text()')
        item = ArtistParsed()
        item['artist'] = hxs.select('//div[@id="artist_title"]/span/a/text()').extract()[0]
#        print item['artist']
        item.save()
        return item