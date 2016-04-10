from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import scrapy

from scrapmanga.items import ScrapmangakuItem, MyImage


class MangakuSpider(scrapy.Spider):
    name = "manga"
    start_urls = (
        'http://www.mangagebo.com/baca-komik-one-piece-terbaru/',
    )

    def __init__(self, manga_url):
        self.start_urls = (manga_url, )

    def parse(self, response):
        results = response.selector.xpath('//ul[@class="lcp_catlist"]/li')

        for result in results:
            item = ScrapmangakuItem()
            item['name'] = result.xpath('a/text()').extract_first().encode('ascii', 'ignore')
            item['url'] = result.xpath('a/@href').extract_first().encode()

            url = result.xpath('a/@href').extract_first().encode()
            request = scrapy.Request(url, callback=self.fetch_item, meta=item)

            yield request

    def fetch_item(self, response):
        images = response.xpath('//div[@class="entry-content"]//img')
        images_urls = []
        for image in images:
            image_url = image.xpath('@src').extract_first()
            images_urls.append(image_url)

        image = MyImage()
        image['images_urls'] = images_urls
        image['images'] = response.meta
        return image


