# -*- coding: utf-8 -*-

import scrapy

from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from ptc_crawler.items import Sign

from ptc_crawler.constants.ptc_constants import signs
from ptc_crawler.constants.ptc_constants import others

from ptc_crawler.constants.ptc_constants import domain
from ptc_crawler.constants.ptc_constants import base_item
from ptc_crawler.constants.ptc_constants import base_sign

class SignsSpider(scrapy.Spider):
	name= "signs"	

	def __init__(self):
		self.others_link=domain+base_item
		self.signs_link=domain+base_sign

	def start_requests(self):
		signs_links=[self.signs_link+sign for sign in signs]
		others_links=[self.others_link+sign for sign in others]
		
		categories=signs+others
		links=signs_links+others_links

		for index, signs_link in enumerate(links):
			yield scrapy.Request(url=signs_link, callback=self.parse, meta={'current_category': categories[index]})

	def parse(self, response):
		category=response.meta['current_category']

		link_loader=ItemLoader(response=response)
		links=link_loader.get_css('div.main > section.section > div.container > div > div > div > a')
		
		for link in links:
			link_selector=Selector(text=link, type="xml")
			link_loader=ItemLoader(item=Sign(), selector=link_selector)
			
			link_loader.add_value('category', category)
			link_loader.add_xpath('detail_url', '@href')
			link_loader.add_xpath('meaning', '@title')
			link_loader.add_xpath('miniature_url', 'img/@src')			
			
			sign=link_loader.load_item()
			yield scrapy.Request(url=sign['detail_url'], callback=self.parse_image_url, meta={'current_item': sign})

	def parse_image_url(self, response):
		image_loader=ItemLoader(response=response)
		link=image_loader.get_css('div.main > section.section > div.container > div > div > div > img')[0]

		link_selector=Selector(text=link, type="xml")
		sign=response.meta['current_item']
		link_loader=ItemLoader(item=sign, selector=link_selector)

		link_loader.add_xpath('image_url', '@src')
		
		sign=link_loader.load_item()
		return sign
		
