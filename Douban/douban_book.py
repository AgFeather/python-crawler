#爬取豆瓣关于python书籍的信息
#使用urllib.request.urlretrieve()下载书籍图片


class Douban(object):
	"""docstring for Douban"""
	def __init__(self):
		self.url = "http://read.douban.com/search?q=Python&start="

	def get_html(self):
		headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
		response = requests.get(self.url,headers = headers)
		response.encoding = 'utf-8'
		return response.text

	def html_parser(self,html):
		soup = BeautifulSoup(html,'lxml')
		book_list = soup.find_all('li',class_='item store-item')


		book_title = []
		book_author = []
		book_comment = []
		comments_more = []
		img_urls = []

		for book in book_list:
			title = book.find('div',class_='title').find('a').text
			author = book.find('a',class_='author-item').text
			comment = book.find('div',class_='article-desc-brief').text

			comment_more = book.find('div',class_='article-desc-brief').find('a').get("href")
			comments_more.append('http://read.douban.com'+str(comment_more))
			
			img = book.find('img').get('src')
			book_title.append(title)
			book_author.append(author)
			book_comment.append(comment)
			img_urls.append(img)

		self.info_download(book_title,book_author,book_comment)
		self.img_download(img_urls)


	def info_download(self,title,author,comment):
		with open('Douban_book.txt','w') as write:
			for a,b,c in zip(title,author,comment):
				write.write('{}   {}\n{}\n\n\n'.format(a,b,c))


	def img_download(self,imgs):
		imgID = 0
		file_path = 'img'
		if not os.path.exists(file_path):
			os.mkdir(file_path)
		for img in imgs:
			download = urllib.request.urlretrieve(img,"{}/{}.jpg".format(file_path,imgID))
			imgID+=1
		
