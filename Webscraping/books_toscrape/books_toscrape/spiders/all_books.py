# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


def product_info(response, value):
    return response.xpath('//th[text()="' + value + '"]/following-sibling::td/text()').extract_first()

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
        yield Request(absolute_next_page_url)

    def parse_book(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()
        image_url = response.xpath('//img/@src').extract_first()
        image_url = image_url.replace('../..', 'http://books.toscrape.com')

        rating = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
        rating = rating.replace('star-rating', '')

        description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()

        # Product information data-points
        upc = product_info(response, 'UPC')
        product_type = product_info(response, 'Product Type')
        price_without_tax = product_info(response, 'Price (excl. tax)')
        price_with_tax = product_info(response, 'Price (incl. tax)')
        tax = product_info(response, 'Tax')
        availability = product_info(response, 'Availability')
        reviews = product_info(response, 'Number of reviews')

        yield {
            'title' : title,
            'price' : price,
            'image_url' : image_url,
            'rating' : rating,
            'description' : description,
            'upc' : upc,
            'product_type' : product_type,
            'price_without_tax' : price_with_tax,
            'price_with_tax' : price_with_tax,
            'tax' : tax,
            'availability' : availability,
            'reviews' : reviews
        }
