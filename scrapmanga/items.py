# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapmangakuItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()


class MyImage(scrapy.Item):
    images_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
