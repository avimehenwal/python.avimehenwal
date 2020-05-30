# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesToscrapePipeline(object):
    def process_item(self, item, spider):
        if item['h1_tags']:
        	item['h1_tags'] = item['h1_tags'][0].upper()
        if item['tags']:
        	item['tags'] = [tag.upper() for tag in item['tags']]
        return item
