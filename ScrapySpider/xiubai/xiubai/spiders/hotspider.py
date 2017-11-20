# -*- coding: utf-8 -*-
import scrapy
from xiubai.items import XiubaiItem

class HotspiderSpider(scrapy.Spider):
    name = 'hotspider'
    allowed_domains = ['qiushibaike.com']
    start_urls = []
    for i in range(1,5):
    	start_urls.append('http://qiushibaike.com/8hr/page/'+str(i)+'/')

    def parse(self, response):
        item = XiubaiItem()

        main = response.xpath('//div[@id="content-left"]/div')

        for div in main:
        	item['author'] = div.xpath('.//h2/text()').extract()[0]
        	item['body'] = ''.join(div.xpath('a[@class="contentHerf"]/div/span[1]/text()').extract()[0])
        	item['funNum'] = div.xpath('.//span[@class="stats-vote"]/i/text()').extract()[0]
        	item['comNum'] = div.xpath('.//span[@class="stats-comments"]/a/i/text()').extract()[0]
        	yield item
