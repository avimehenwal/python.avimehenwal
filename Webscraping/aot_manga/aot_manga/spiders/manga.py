# -*- coding: utf-8 -*-
import scrapy


class MangaSpider(scrapy.Spider):
    name = 'manga'
    allowed_domains = ['readsnk.com/']
    start_urls = ['https://ww7.readsnk.com/']

    def parse(self, response):
        selector = "body > div.container.px-3.mx-auto > div > div.w-full.md\:w-2\/3.px-2 > div:nth-child(4) > div > div.flex.flex-col > a::text"
        latest_chapter = response.css(selector).re(r'\d+')[0]
        self.logger.info('Latest Chapter = %s', latest_chapter)


