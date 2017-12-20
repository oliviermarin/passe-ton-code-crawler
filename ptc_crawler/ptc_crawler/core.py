# -*- coding: utf-8 -*-

import scrapy

from scrapy import spiderloader
from scrapy.utils import project
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from twisted.internet import reactor

settings=project.get_project_settings()
spider_loader=spiderloader.SpiderLoader.from_settings(settings)
signs_spider=spider_loader.load('signs')


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()
d = runner.crawl(signs_spider)
d.addBoth(lambda _: reactor.stop())
reactor.run()

