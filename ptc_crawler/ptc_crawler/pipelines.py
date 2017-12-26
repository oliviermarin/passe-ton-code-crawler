# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import logging
import json
import urllib

from ptc_crawler.constants.ptc_constants import signs
from ptc_crawler.constants.ptc_constants import others

import pymongo
from pymongo import MongoClient

class SignPipeline(object):

	def __init__(self, server, port, sign_img_dir):
		self.crawling_results=[]
		self.logger=logging.getLogger(__name__)
		self.client=MongoClient(server, port);
		self.db=self.client.passeTonCode
		self.sign_img_dir=sign_img_dir
	
	@classmethod
	def from_crawler(cls, crawler):
		settings = crawler.settings
		return cls(settings['MONGODB_SERVER'], settings['MONGODB_PORT'], settings['SIGNS_IMG_DIR'])

	def open_spider(self, spider):
		self.logger.info('spider has opened')

	def close_spider(self, spider):
		self.logger.info('spider has closed')
		self.logger.info(json.dumps(self.crawling_results, indent=4, sort_keys=True))
		self.db.signs.insert(self.crawling_results)
		self.client.close()

	def process_item(self, item, spider):
		miniature_uri=self.sign_img_dir+'miniature/'+item['category']+'/'+item['miniature_url'].rsplit('/', 1)[-1]
		image_uri=self.sign_img_dir+'image/'+item['category']+'/'+item['image_url'].rsplit('/', 1)[-1]
		
		urllib.urlretrieve(item['miniature_url'], miniature_uri)
		urllib.urlretrieve(item['image_url'], image_uri)

		self.crawling_results.append({
				'category': item['category'], 
				'meaning': item['meaning'], 
				'miniature_url': item['miniature_url'],
				'miniature_uri': miniature_uri, 
				'image_url': item['image_url'],
				'image_uri': image_uri
			})
