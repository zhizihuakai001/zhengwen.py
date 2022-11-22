import time

import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://5gya.buzz/h/日韩'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}


def index():
    html = requests.get(url=url , headers=headers).text
    # print(html)

    # 获取该网页所有视频的编号
    soup = BeautifulSoup(html , 'html.parser')
    items = soup.find_all('a' , title="点击在线播放")
    gril = soup.find_all('img')
    return items , gril

    # 获取所有视频的名字存入指定的data列表


def web(items , gril):
    data = []
    for i in gril:

        alt = i.get('alt')
        if alt:
            data.append(alt)
    url_1s = []
    names = []
    for i , name in zip(items , data):
        # alt = alts.find('img')
        # print(i['href'])
        # win = etree.HTML(html).xpath('//a[@href="97582"]/text')
        # print(win)
        # 拼接视频的网站地址
        url_0 = 'https://5gyn.buzz{}'.format(i['href'])

        # 把拼接好的视频地址用起来，进入播放页面，用lxml.etree.xpath找出该页面视频下载地址编号，并拼接上
        html_0 = requests.get(url=url_0 , headers=headers).text
        win = etree.HTML(html_0)
        win_0 = win.xpath('//span[@id="downloadurl"]/text()')
        # print(win_0[0])
        url_1 = "https://5gmtf.xyz/mp4/{}".format(win_0[0])
        names.append(name)
        url_1s.append(url_1)
    return names , url_1s


def download(name , url_1s):
    for name , url_1 in zip(name , url_1s):
        f = open('C:/Users/HP/Desktop/pa-chong/{}.mp4'.format(name) , 'w')
        download = requests.get(url=url_1 , headers=headers)
        # downloads = download.content

        print('正在下载{}'.format(name))
        time.sleep(5)
        f.write(download.content.decode('utf8'))
        print('下载完成慢慢欣赏吧' , end='/n')
        f.close()


if __name__ == '__main__':
    items , gril = index()
    names , url_1s = web(items=items , gril=gril)
    print('下载路径以爬取')
    # time.sleep(100)
    # web(items=items , gril=gril)
    download(name=names , url_1s=url_1s)
