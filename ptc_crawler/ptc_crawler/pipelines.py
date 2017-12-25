# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import logging
import json

from ptc_crawler.constants.ptc_constants import signs
from ptc_crawler.constants.ptc_constants import others

import pymongo
from pymongo import MongoClient

class SignPipeline(object):

	def __init__(self, server, port):
		self.crawling_results=[]
		self.logger=logging.getLogger(__name__)
		self.client = MongoClient(server, port);
		self.db = self.client.passeTonCode
	
	@classmethod
	def from_crawler(cls, crawler):
		settings = crawler.settings
		return cls(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])

	def open_spider(self, spider):
		self.logger.info('spider has opened')

	def close_spider(self, spider):
		self.logger.info('spider has closed')
		self.logger.info(json.dumps(self.crawling_results, indent=4, sort_keys=True))
		self.db.signs.insert(self.crawling_results)
		self.client.close()

	def process_item(self, item, spider):
		self.crawling_results.append({
				'category': item['category'], 
				'meaning': item['meaning'], 
				'miniature': item['miniature_url'],
				'image': item['image_url']
			})
