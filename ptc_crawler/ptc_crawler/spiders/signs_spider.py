# -*- coding: utf-8 -*-

import scrapy

from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from ptc_crawler.items import Sign

class SignsSpider(scrapy.Spider):
	name= "signs"

	def start_requests(self):
		urls=['http://www.passetoncode.fr/panneaux-de-signalisation/panneaux/agglomeration/']
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		linkLoader=ItemLoader(response=response)
		links=linkLoader.get_css('div.main > section.section > div.container > div > div > div > a')
		for link in links:
			linkSelector=Selector(text=link, type="xml")
			linkLoader=ItemLoader(item=Sign(), selector=linkSelector)
			
			linkLoader.add_xpath('detail_url', '@href')
			linkLoader.add_xpath('meaning', '@title')
			linkLoader.add_xpath('miniature_url', 'img/@src')			
			
			sign=linkLoader.load_item()
			self.log(sign)
