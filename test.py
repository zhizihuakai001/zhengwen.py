from urllib.request import urlopen


html = urlopen('https://www.googletagmanager.com/gtag/js?id=G-1YMQC5WFBC').read().decode('utf-8')
print(html)
