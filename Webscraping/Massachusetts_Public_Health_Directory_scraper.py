# -*- coding: utf-8 -*-

"""
AUTHOR  : avimehenwal
DATE    : Wed Sep 27 17:00:11 IST 2017
PURPOSE : http://member.mahb.org/Directory_BOH.aspx?Login=173

"""

import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.exceptions import CloseSpider

URL = 'http://member.mahb.org/Directory_BOH_Browse.aspx?opt={}' #1-5

class NaviSpider(scrapy.Spider):
    name = 'navi'
    allowed_domains = ['member.mahb.org']
    start_urls = [ URL.format(i) for i in range(1,6)]
    #start_urls = [ URL.format(i) for i in range(3,4)]

    def parse(self, response):
        if response.status != 200:
            self.logger.critical('ERROR LOADING PAGE')
            open_in_browser(response)
            raise CloseSpider('bandwidth_exceeded')
        open_in_browser(response)
        links = response.xpath('//table//td/a[@class="town"]/@href').extract()
        for link in links:
        #for link in links[:2]:
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        address = response.xpath("//span[contains(@id,'Address')]/text()").extract_first()
        city    = response.xpath("//span[contains(@id,'City')]/text()").extract_first()
        zipcode = response.xpath("//span[contains(@id,'name')]/text()").extract_first()
        phone   = response.xpath("//span[contains(@id,'Phone')]/text()").extract_first()
        g_email = response.xpath("//span[contains(@id,'Email')]/text()").extract_first()
        web     = response.xpath("//span[contains(@id,'Website')]/text()").extract_first()

        members = response.xpath("//span[contains(@id,'member')]//tr")
        for member in members:
            name = member.xpath('.//td[1]/text()').extract_first()
            position = member.xpath('.//td[2]/text()').extract_first()
            p_email = member.xpath('.//td[3]/text()').extract_first()

            if p_email:
                email = p_email
            else:
                email = g_email

            results = {
                "Name": name,
                "Position": position,
                "Address": address,
                "City": city ,
                "Zip": zipcode,
                "Phone": phone,
                "Email": email,
                "Website": web,
                "URL" : response.url,
            }
            yield results
