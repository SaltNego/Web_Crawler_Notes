# coding:utf-8
from selenium import webdriver

url = 'https://www.taobao.com'
chrome_options = webdriver.ChromeOptions()
# 加载自己的chrome浏览器配置
chrome_options.add_argument('--user-data-dir=C:/Users/Negoowen/AppData/Local/Google/Chrome/User Data')
brower = webdriver.Chrome(chrome_options=chrome_options)
brower.get(url)