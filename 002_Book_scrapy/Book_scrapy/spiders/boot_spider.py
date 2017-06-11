# -*-coding:utf-8-*-
import scrapy

class BooKsSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()
            yield{
                'name': name,
                'price':price,
            }
        nextPage = response.css('ul.pager li.next a::attr(href)').extract_first()
        if nextPage:
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage,callback = self.parse)