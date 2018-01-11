# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from douban.items import DoubanItem


class TopspiderSpider(scrapy.Spider):
	name = 'topspider'
	allowed_domains = ['https://book.douban.com/top250?start=']
	url = 'http://book.douban.com/top250?start='
	start_urls = []
	for i in range(0,250,25):
		start_urls.append(url+str(i))

	def parse(self, response):
		item = DoubanItem()
		soup = BeautifulSoup(response.text,'lxml')
		content = soup.find_all('tr',class_='item')
		for book in content:
			item['title'] = book.find('div',class_='pl2').find('a')["title"]
			item['author'] = book.find('p',class_='pl').get_text()
			item['star'] = book.find('span',class_='rating_nums').get_text()
			item['brief'] = book.find('span',class_='inq').get_text()
			item['img'] = book.find('img').get('src')
			yield item

