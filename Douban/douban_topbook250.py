#爬去豆瓣top书籍250榜单，并下载图片，保存书籍信息

class TopBook250(object):
	"""docstring for TopBook250"""
	def __init__(self):
		self.headers = {
			'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
		}
		self.url_basic = "https://book.douban.com/top250?start="
		self.url_list = []
		for i in range(0,250,25):
			self.url_list.append(self.url_basic+str(i))
		self.get_html()
		self.html_parser()
		self.download()

	def get_html(self):
		self.html_list = []
		for url in self.url_list:
			response = requests.get(url,headers = self.headers)
			self.html_list.append(response.text)

	def html_parser(self):
		self.book_title = []
		self.book_author = []
		self.book_star = []
		self.book_brief = []
		self.book_img = []
		for html in self.html_list:
			soup = BeautifulSoup(html,'lxml')
			content = soup.find_all('tr',class_='item')
			for book in content:
				try:
					title = book.find('div',class_='pl2').find('a')["title"]
					author = book.find('p',class_='pl').get_text()
					star = book.find('span',class_='rating_nums').get_text()
					brief = book.find('span',class_='inq').get_text()
					img = book.find('img').get('src')
					self.book_title.append(title)
					self.book_author.append(author)
					self.book_star.append(star)
					self.book_brief.append(brief)
					self.book_img.append(img)
				except:
					print("exception")
				

	def download(self):
		file_path = 'book_info'
		imgID = 0
		if not os.path.exists(file_path):
			os.mkdir(file_path)
		
		with open('{}/TopBook250.txt'.format(file_path),'a') as f:
			for title,author,star,brief,img in zip(self.book_title,self.book_author,self.book_star,self.book_brief,self.book_img):
				f.write('{}\n{}   {}\n{}\n\n'.format(title,author,star,brief)) 
			urllib.request.urlretrieve(img,'{}/{}.jpg'.format(file_path,imgID)) 
			imgID+=1
