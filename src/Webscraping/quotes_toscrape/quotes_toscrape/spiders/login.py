# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from quotes_toscrape.items import QuotesToscrapeItem

from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class LoginSpider(Spider):
    name = "login"
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        return FormRequest.from_response(response,
            formdata={'csrf_token' : token,
                        'password'   : 'foobar',
                        'username'   : 'foobar'},
            callback=self.scrape_home_page)

    def scrape_home_page(self, response):
        open_in_browser(response)
        l = ItemLoader(item=QuotesToscrapeItem(), response=response)
        tags    = response.xpath("//*[@class='tag-item']/a/text()").extract()
        h1_tags = response.xpath('//h1/a/text()').extract_first()
        
        l.add_value('tags', tags)
        l.add_value('h1_tags', h1_tags)
        
        return l.load_item()
