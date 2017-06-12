# -*-coding:utf-8-*-
import scrapy
import re

from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle

from doubanbook.items import DoubanbookItem

class DoubanbookSpider(CrawlSpider):
    name = "book"
    allowed_domains = ["douban.com"]
    start_urls = ['https://book.douban.com/tag/%E7%BB%8F%E5%85%B8']
    rules = [
        Rule(sle(allow=("/subject/\d+/$")), callback='parse_2'),
        #Rule(sle(allow=("/tag/[^/]+", )), follow=True),
        #Rule(sle(allow=("/tag/$", )), follow=True),
    ]
    def parse_2(self, response):
        for i,book in enumerate(response.css('#wrapper')):
            item = DoubanbookItem()
            item['rate_num'] = book.xpath('.//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
            if round(float(item['rate_num'].strip())) >= 7:
                item['name'] =book.xpath('.//h1/span/text()').extract_first()
                yield item
'''
    def parse(self, response):
        item = DoubanbookItem()
        for i,book in enumerate(response.css('#wrapper')):
            item['name'] = book.xpath('./div/h1/text()').extract_first()
            yield item
        '''
'''
        for i in range(2,50):
            nextPage = "http://www.xiaohuar.com/list-1-"+str(i)+".html"
            if nextPage:
                nextPage = response.urljoin(nextPage)
                yield scrapy.Request(nextPage, callback = self.parse)
        '''
