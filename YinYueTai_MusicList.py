import requests
from bs4 import BeautifulSoup


#通过限定User_agent反爬虫
def get_agent():
    '''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    '''
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
    return fakeheader

#通过限制访问IP反爬虫
def get_proxy():
    '''
    简答模拟代理池
    返回一个字典类型的键值对，
    '''
    proxy = ["http://116.211.143.11:80",
             "http://183.1.86.235:8118",
             "http://183.32.88.244:808",
             "http://121.40.42.35:9999",
             "http://222.94.148.210:808"]
    fakepxs = {}
    fakepxs['http'] = proxy[random.randint(0, len(proxy))]
    return fakepxs

#通过定义JS脚本来反爬虫，终极方法，
#如验证码，滑块，要求浏览器通过js计算一段数字和等方法
#解决方法：使用PhantomJSP，是一个python包，可以在没有图形解界面的情况下，完全模拟一个浏览器




def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except Exception as e:
        e.message()
        
def htmlParser(html):
    music_info = []
    soup = BeautifulSoup(html,'lxml')
    music_list = soup.find_all('div',attrs={'name':'scrollArea'})
    for music in music_list:
        music_one = {}
        score = music.find('h3',attrs={'class':'asc_score'})
        if score == None:
            score = music.find('h3',class_='desc_score').text.strip()
        else:
            score = score.text.strip()
        top_num = music.find('div',class_='top_num').text.strip()
        music_name = music.find('a',class_='mvname').text.strip()
        author = music.find('a',class_='special').text.strip()
        time = music.find('p',class_='c9').text.strip()
        music_one['score'] = score
        music_one['top_num'] = top_num
        music_one['author'] = author
        music_one['time'] = time
        music_one['music_name'] = music_name
        music_info.append(music_one)
    return music_info
        
        
    
    
    
    
    
    
if __name__ == '__main__':
    areas = ['ML','HT','US','JP','KR']
    for area in areas:
        url = 'http://vchart.yinyuetai.com/vchart/trends?area='+area
        html = get_html(url)
        music_list = htmlParser(html)
        for music in music_list:
            print(music)
    
    
    
    
