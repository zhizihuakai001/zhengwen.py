import requests
import re
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
data = [1, 2]
# for i in data:
url = 'https://5gxy.buzz/97562/'

h = requests.get(url).text
b = requests.get(url).content.decode('utf-8')
url2 = re.findall('https://5gmtf.xyz/', h)
html = BeautifulSoup(h, 'lxml')
print(html)

#print(h)
#print('------------------------------>' + b)

#print(url2)