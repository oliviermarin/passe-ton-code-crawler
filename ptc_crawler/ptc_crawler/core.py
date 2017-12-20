# -*- coding: utf-8 -*-

import scrapy

from scrapy import spiderloader
from scrapy.utils import project
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from constants.ptc_constants import signs

settings=project.get_project_settings()
spider_loader=spiderloader.SpiderLoader.from_settings(settings)

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

signs_spider=spider_loader.load('signs')
signs_spider.custom_settings['SIGNS'] = signs

runner = CrawlerRunner()
crawling_process=runner.crawl(signs_spider)
crawling_process.addBoth(lambda _: reactor.stop())

reactor.run()

