# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         test
# Author:       Negoowen
# Date:         2020/3/9
__Author__ = 'Negoo_wen'
#-------------------------------------------------------------------------------
import requests
import csv
from lxml import etree
from fake_useragent import UserAgent


ua = UserAgent().random
headers = {
    'User-Agent':ua
}
def main():
    try:
        for page in range(1,276):
            print('=======================Running>>>' + str(page))
            tar_url = 'http://x.x.x.x/?02104&page='+str(page)
            req = requests.get(tar_url,headers = headers)
            readText = req.text
            #print readText
            #正则表达式

            html = etree.HTML(readText)
            infos = html.xpath('//*[@id="g-wp"]/div[5]/div[2]/table/tbody/tr[1]/following-sibling::tr/*')
            print(len(infos))
            a = []
            for info in infos:
                a.append(info.text)
            step = 6
            b = [a[i:i+step] for i in range(0,len(a),step)]


            for i in b:
                persons = str(i).replace('u','').replace('\'','')
                print(persons)
                with open('persons.csv', 'a', encoding='utf8') as f:
                    f.write(persons + '\n')
        f.close()
    except Exception as e:
        print('======================================================error!!!>>>' + str(page))
        print(str(e))
        pass

if __name__ == '__main__':
    main()

