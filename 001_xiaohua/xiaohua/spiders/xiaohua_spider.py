# -*-coding:utf-8-*-
import scrapy
from scrapy.crawler import CrawlerProcess
from xiaohua.items import XiaohuaItem
class XiaohuaSpider(scrapy.Spider):
    name = "xiaohua"
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']
    
    def parse(self, response):
        item = XiaohuaItem()
        for i,book in enumerate(response.css('div.img')):
            item['image_urls'] = book.xpath('./a/img/@src').extract_first()
            item['name'] = book.xpath('./a/img/@alt').extract_first()
            yield item
        for i in range(2,50):
            nextPage = "http://www.xiaohuar.com/list-1-"+str(i)+".html"
            if nextPage:
                nextPage = response.urljoin(nextPage)
                yield scrapy.Request(nextPage, callback = self.parse)
