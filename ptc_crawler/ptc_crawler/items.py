# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class Sign(scrapy.Item):
	detail_url = scrapy.Field(output_processor=TakeFirst())
	meaning = scrapy.Field(output_processor=TakeFirst())
	miniature_url = scrapy.Field(output_processor=TakeFirst())
