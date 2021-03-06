# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    save_prefix = scrapy.Field()

class BingItem(scrapy.Item):
    href = scrapy.Field()
    save_prefix = scrapy.Field()
