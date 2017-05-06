# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class AllBooksSpider(scrapy.Spider):
    name = "all_books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # process next page
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request()

    def parse_book(self, response):
        pass
