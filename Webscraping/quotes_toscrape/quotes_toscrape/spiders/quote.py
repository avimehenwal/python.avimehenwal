# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class QuoteSpider(Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]        # valid domain
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
        	text   = quote.xpath('.//*[@class="text"]/text()').extract_first()
        	author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
        	tags   = quote.xpath('.//*[@class="tag"]/text()').extract()

        	yield {
        		'Text'   : text,
        		'Author' : author,
        		'Tags'   : tags
        	}

    	# crawling Next page for run the same spider
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)       # callback