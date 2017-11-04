#使用python3 requests和bs4 下载‘http://www.qu.la/paihangbang’小说排行榜下的所有小说

import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # check response status 200 means successful
        response.encoding = 'utf-8'
        return response.text
    except:
        return 'html error'


#获取各个排行榜所有小说的url并返回，同时创建
def get_content(html):
    url_list = []
    soup = BeautifulSoup(html,'lxml')
    category_list = soup.find_all('div',attrs={'class':'index_toplist mright mbottom'})#获取各个排行榜
                            #测试时将find_all 改为find加快测试速度

    for cate in category_list:
        name = cate.find('div',class_='toptab').span.string
        with open('novel_list.csv','a+') as f:
            f.write('\ntype of novel:{}\n'.format(name))#获取当前排行榜名字，并写入csv中
            novel_list = cate.find_all('a')#获取当前排行榜所有小说的href
            for novel in novel_list:
                novel_url = 'http://www.qu.la'+novel['href']#讲每个小说的url拼接完整
                novel_title = novel['title']
                url_list.append(novel_url)#将这个小说的url放入返回list中
                with open('novel_list.csv','a') as f:#讲小说名，以及小说的url保存在csv中
                    f.write('novel_name:{:<}\t novel_url:{:<}\n'.format(novel_title,novel_url))
    return url_list


#获取每个小说的所有章节url并返回，同时返回小说名
def get_txt_url(url):
    url_list=[]
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    chaper_list = soup.find_all('dd')
    txt_name = soup.find('h1').text
    try:
        with open('{}.txt'.format(txt_name),'a+') as f:#生成一个以小说名命名的txt文件
            f.write('novel title:{}\n'.format(txt_name))
            for chaper in chaper_list:
                url_list.append('http://www.qu.la/'+chaper.find('a')['href'])#讲每个章节的url拼接完整
    except Exception as e:
        print(e)
    return url_list,txt_name


#根据小说所有章节的url，讲所有章节内容写入到已经创建好的txt文件中
def get_one_txt(url,txt_name):
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    content = soup.find('div',attrs={'id':'content'}).text.replace('chaptererror();','')
    title = soup.find('title').text

    with open('{}.txt'.format(txt_name),'a+') as f:
        f.write(title+'\n\n')
        f.write(content)
        print('the novel:{} the chapter:{} has been downloaded'.format(txt_name,title))







if __name__ == '__main__':
    url = 'http://www.qu.la/paihangbang'#起始页，包含数个排行榜
    html = get_html(url)
    
    novel_url_list = get_content(html)#获取起始页排行榜内的所有小说的url
    for novel_url in novel_url_list:
        chapter_url_list,txt_name = get_txt_url(novel_url)#对每个小说，获取所有章节的url
        for chapter in chapter_url_list:
            get_one_txt(chapter, txt_name)#对每个章节进行下载


    #test 测试用，单独下载第一个小说
#     novel_url = novel_url_list[0]
#     chapter_url_list, txt_name = get_txt_url(novel_url)
#     for chapter in chapter_url_list:
#         get_one_txt(chapter, txt_name)



