import requests
from bs4 import BeautifulSoup
from lxml import etree
import os

from requests import post

url = 'https://5gxz.buzz/34835/'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
html = requests.get(url=url , headers=headers)
html1 = etree.HTML(html.text)
ul = html1.xpath('//li[@class="pin"]/a/@href')
print(ul)  # ['/82258/', '/73764/', '/31854/', '/47494/', '/79555/', '/70478/', '/69574/', '/83328/']
i = ul[0]
url2 = 'https://5gxz.buzz' + i
html_1 = requests.get(url=url2 , headers=headers)
html_2 = etree.HTML(html_1.content)
ul_ = html_2.xpath('//span[@id="downloadurl"]/text()')
print(ul_[0])
ul_1 = html_2.xpath('//title/text()')
print(ul_1)

url_2 = "https://5gmtf.xyz/mp4/{}".format(ul_[0])
print(url_2)

with open("{}.video".format(ul_1) , 'wb') as f:
    downloads = requests.get(url=url_2 , headers=headers)
    p = downloads.content
    f.write(p)


