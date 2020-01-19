# coding:utf-8
# 获取电影票房排行榜前五十
__Author__ = 'Negoo_wen'
import requests
from lxml import etree

url = 'http://58921.com/alltime/wangpiao'
def main():
    html = requests.get(url).content
    tree = etree.HTML(html)
    box = tree.xpath('//*[@class="odd" or @class="even"]/td[2]/a/text()')
    for i in range(len(box)):
        print str(i+1)+" :  " + box[i]

if __name__ == '__main__':
    main()