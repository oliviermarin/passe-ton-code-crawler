# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy

class SignPipeline(object):
	
	def open_spider(self, spider):
		print 'spider {} has opened'.format(spider.__class__.__name__)

	def close_spider(self, spider):
		print 'spider {} has closed'.format(spider.__class__.__name__)

	def process_item(self, item, spider):
		print item


