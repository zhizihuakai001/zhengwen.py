import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://5gya.buzz/h/日韩'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
html = requests.get(url=url , headers=headers).text
# with open('shou_ye.html', 'w', encoding='utf-8') as f:
# f.write(html)
a = etree.HTML(html)
b = a.xpath('//a/text')
print(a)


soup = BeautifulSoup(html, 'html.parser')
gril = soup.find_all('img')

for i in gril:
    alt = i.get('alt')
    data = []
    if alt:
        data.append(alt)

