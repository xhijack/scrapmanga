# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy

from slugify import slugify
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class MyImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return "{}/{}".format(request.meta['dir'], image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['images_urls']:
            yield scrapy.Request(image_url, meta={'dir':slugify(item['images']['name'])})

    def item_completed(self, results, item, info):
        image_paths = [x['url'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
