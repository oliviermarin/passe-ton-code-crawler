# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, Compose
from constants.ptc_constants import domain

class Sign(scrapy.Item):
	category=scrapy.Field(output_processor=TakeFirst())
	detail_url=scrapy.Field(output_processor=Compose(lambda v: v[0], lambda uri: domain+uri))
	meaning=scrapy.Field(output_processor=TakeFirst())
	miniature_url=scrapy.Field(output_processor=TakeFirst())
	image_url=scrapy.Field(output_processor=TakeFirst())
