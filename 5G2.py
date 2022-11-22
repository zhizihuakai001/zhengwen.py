import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://5gxz.buzz/34835/'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
html = requests.get(url=url, headers=headers)
# with open('5g.html', 'wb') as stream:
  #  stream.write(html.content)
with open('5g.html', 'r', encoding='UTF-8') as stream:
    all = stream.read()
    html1 = etree.HTML(all)
    ul = html1.xpath('//span[@id="downloadurl"]/text()')
    #ul2 = html1.xpath('//div[@class="b_t"]/text()')
    url3 = html1.xpath('//title/text()') #
    print(url3) #['5G影院 - 天天5g天天爽 - 22a 淫荡的补习眼镜老师 趁着补习时间不断勾引着学生摩擦发育的阴茎含住直接观音坐莲上去摩擦']
    # print(ul2) [' > ', '22a 淫荡的补习眼镜老师 趁着补习时间不断勾引着学生摩擦发育的阴茎含住直接观音坐莲上去摩擦']
    print(ul)
