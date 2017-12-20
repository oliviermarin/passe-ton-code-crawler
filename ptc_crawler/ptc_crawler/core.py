# -*- coding: utf-8 -*-

import scrapy
import time

from scrapy import spiderloader
from scrapy.utils import project
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from constants.ptc_constants import signs
from scrapy.crawler import CrawlerProcess

settings=project.get_project_settings()
spider_loader=spiderloader.SpiderLoader.from_settings(settings)

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

signs_spider=spider_loader.load('signs')
signs_spider.custom_settings['SIGNS']=signs

process=CrawlerProcess()
process.crawl(signs_spider)

items_signs=signs_spider.custom_settings['ITEMS_SIGNS']

process.start()

for items_sign in items_signs:
	print items_sign




