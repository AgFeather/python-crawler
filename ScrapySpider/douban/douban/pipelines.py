# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from douban.items import DoubanItem
import urllib

imgID = 0

class DoubanPipeline(object):
	def process_item(self, item, spider):
		file_path = 'book_info'
		global imgID
		if not os.path.exists(file_path):
			os.mkdir(file_path)
		with open('{}/TopBook250.txt'.format(file_path),'a') as f:
			f.write('{}\n{}\n{}\n{}\n\n\n'.format(item['title'],item['star'],item['author'],item['brief']))
		urllib.request.urlretrieve(item['img'],'{}/{}.jpg'.format(file_path,imgID))
		imgID+=1
		return item
