import requests
from bs4 import BeautifulSoup

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
    
    
    
    
