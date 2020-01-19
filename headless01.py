# coding:utf-8
from selenium import webdriver

url = 'https://www.taobao.com'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')#无界面设置
chrome_options.add_argument('--disable-gpu')#不增加，有时定位出错

brower = webdriver.Chrome(chrome_options=chrome_options)
brower.get(url)
print brower.page_source

brower.quit()