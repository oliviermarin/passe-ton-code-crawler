# -*- coding: utf-8 -*-

import scrapy

from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from ptc_crawler.items import Sign
from constants.ptc_constants import signs

class SignsSpider(scrapy.Spider):
	name= "signs"	
	signs_link='http://www.passetoncode.fr/panneaux-de-signalisation/panneaux/'
	
	custom_settings={
        'SIGNS': []
    }

	#def __init__(self):
	#	self.signs = signs		

	def start_requests(self):
		# signs_links=[self.signs_link+sign for sign in self.signs]
		signs_links=[self.signs_link+sign for sign in self.custom_settings['SIGNS']]
		for signs_link in signs_links:
			yield scrapy.Request(url=signs_link, callback=self.parse)

	def parse(self, response):
		link_loader=ItemLoader(response=response)
		links=link_loader.get_css('div.main > section.section > div.container > div > div > div > a')
		for link in links:
			link_selector=Selector(text=link, type="xml")
			link_loader=ItemLoader(item=Sign(), selector=link_selector)
			
			link_loader.add_xpath('detail_url', '@href')
			link_loader.add_xpath('meaning', '@title')
			link_loader.add_xpath('miniature_url', 'img/@src')			
			
			sign=link_loader.load_item()
			self.log(sign)
