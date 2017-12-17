#因为煎蛋网站为防止爬虫，对于ooxx图片使用了js加载，用普通的requests方法爬取图片url的话，会发现返回的url都是blank
#所以这里使用selenium模拟浏览器方法爬取图片url
#因为使用selenium，所以导致爬取非常慢

from selenium import webdriver 

class Jiandan(object):
	"""docstring for Jiandan"""
	def __init__(self):
		self.url = 'http://jandan.net/ooxx'
		self.url_list = []
		for i in range(0,10):
			self.url_list.append(self.url+'/page-'+str(389-i)+'#comments')
		self.parser()


	def parser(self):
		browser = webdriver.PhantomJS()
		self.img_list = []
		self.html_list = []
		imgID = 0
		for url in self.url_list:
			print("parser begin%d"%imgID)
			browser.get(url)
			browser.implicitly_wait(3)
			images = browser.find_elements_by_xpath('//div[@class="text"]/p/img')
			for img in images:
				print("image download begin%d"%imgID)
		#		self.img_list.append(img.get_attribute("src"))
				img_url = img.get_attribute("src")
				self.download(img_url,imgID)
				imgID+=1


	def download(self,url,imgID):
		path = 'image'
		if not os.path.exists(path):
			os.mkdir(path)
		urllib.request.urlretrieve(url,'{}/{}.jpg'.format(path,imgID))
		# for img in self.img_list:
		# 	urllib.request.urlretrieve(img,'{}/{}.jpg'.format(path,imgID))
