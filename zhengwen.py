import requests


def get_num(num):
    url = 'https://cart.taobao.com/cart.htm?spm=a1z02.1.a2109.d1000367.czc9XD&nekot=1470211439694'.format(num)
    html_str = requests.get(url).json()
    # print(html_str)
    datas = html_str['list']
    # print(datas)
    for data in datas:
        print(data)
        name = data['entName']
        leixing = data['prondName']
        beian = data['prondR']
        with open('数据.csv' , 'a+') as file:
            file.write('{}, {}, {}'.format(name , leixing , beian))
            print(name + '下载完成')


for i in range(1000):
    get_num(i)
