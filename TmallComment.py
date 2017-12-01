
#下载天猫商城保暖内衣的评价信息
# 商品评价使用异步加载的json文件
#- 使用chrome开发者工具，network--》json--》进而定位商品评价的json位置
#- 打开该json文件，使用re lib对评价信息进行提取
#- 发现json文件名有规律，所以可以一次爬取多个页面的评价
#- 保存到本地csv文件中，用以进一步数据分析



class TmallComment(object):
	"""docstring for TmallComment"""
	def __init__(self):
		self.nickname = []
		self.ratedate = []
		self.color = []
		self.size = []
		self.ratecontent = []

	def get_urls(self):
		urls = []
		for i in range(1,10):
			url1 = "https://rate.tmall.com/list_detail_rate.htm?itemId=521136254098&spuId=345965243&sellerId=2106525799&order=3&currentPage="
			url2 = "&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hv4vvpvB6vUvCkvvvvvjiPPLqhQjn8R2s9AjljPmPW1jYjPsdhsjtERFswtj189phvHn1w4cm1zYswzmvJ7Ma5zEPw9HuCdphvmZChWx9yvhC9Nu6CvvDvBvh6EQCvxUkrvpvEphRgjnWvphTYdphvmZC2I1LzvhCV0UwCvvBvppvvRphvChCvvvvPvpvhvv2MMQhCvvXvovvvvvmtvpvIphvvDvvvpvHvpCsGvvCCi6CvjvUvvhBGphvwv9vvBj1vpCsGvvChX8yCvv3vpvoCmn%2BJCOyCvvXmp99UVt9EvpCWBxy5v8Wqb6OyCW2lS3p3ZAaorXZzRFWNnHVG62gO4xUkZE7HrX6FpFn79WpaymXLbyzBifwz4Ci%2BV8LrKf%2BiconbInVZSonmWl4vQ8wCvvBvpvpZdphvmZChqHCkvhCfJFyCvvBvpvvv&isg=AunpxHCilzhE1qhJiwAtbioF-JyDHuO8a4UyFIvf1VBrUgxk0wK9ubOAIsAf&needFold=0&_ksTS=1512108949902_948&callback=jsonp949"
			url = url1+str(i)+url2
			urls.append(url)
		return urls
	def get_html(self,urls):
		htmls = []
		for url in urls:
			response = requests.get(url)
			htmls.append(response.text)
		return htmls
	def html_parser(self,htmls):
		for html in htmls:
			self.nickname.extend(re.findall('"displayUserNick":"(.*?)"',html))
			self.color.extend(re.findall(re.compile('颜色分类:(.*?);'),html))
			self.size.extend(re.findall(re.compile('尺码:(.*?);'),html))
			self.ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'),html))
			self.ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'),html))
			print(self.nickname,self.color)
	def download(self):
		file = open("TmallComment.csv",'w')
		for i in list(range(0,len(self.nickname))):
			file.write(','.join((self.nickname[i],self.ratedate[i],self.color[i],self.size[i],self.ratecontent[i]))+'\n')
		file.close()
	def begin(self):
		urls = self.get_urls()
		htmls = self.get_html(urls)
		self.html_parser(htmls)
		self.download()
