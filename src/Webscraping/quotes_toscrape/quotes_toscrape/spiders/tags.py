# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from quotes_toscrape.items import QuotesToscrapeItem

class TagsSpider(scrapy.Spider):
    name = "tags"
    allowed_domains = ["http://quotes.toscrape.com/"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
    	l = ItemLoader(item=QuotesToscrapeItem(), response=response)
    	tags    = response.xpath("//*[@class='tag-item']/a/text()").extract()
    	h1_tags = response.xpath('//h1/a/text()').extract_first()
    	
    	l.add_value('tags', tags)
    	l.add_value('h1_tags', h1_tags)
    	
    	return l.load_item()