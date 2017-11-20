#使用python3 爬去dota2贴吧前50页的所有帖子
#并将标题，链接，发帖人，发帖时间，回复数量保存在一个txt文件中


import requests
from bs4 import BeautifulSoup


def htmlOpen(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except :
        return 'error'

def htmlParser(html):
    soup = BeautifulSoup(html,'lxml')
    comments = []
    liTags = soup.find_all('li', attrs = {'class':" j_thread_list clearfix"} )
    print(len(liTags))
    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find('a',attrs={'class':'j_th_tit'}).text.strip()
            comment['link'] = li.find('a',attrs={'class':'j_th_tit'})['href']
            comment['name'] = li.find('span',attrs={'class':'tb_icon_author'}).text.strip()
            comment['time'] = li.find('span',attrs={'class':'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except Exception as exc:
            print(exc)
    return comments

def outFile(dict):
    with open('comments.txt','a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'],comment['link'],comment['name'],comment['time'],comment['replyNum']
            ))


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/f?kw=dota2&ie=utf-8&pn='
    for i in range(0,10):
        url_ = url+str(i*50)
        print(url_)
        html = htmlOpen(url_)
        datas = htmlParser(html)
        outFile(datas)
    
