# !C:\Python27 python
# -*- coding: UTF-8 -*-
from lxml import etree
import sys
import io
import requests
import HTMLParser

__author__ = 'Allen'
fo = open('./emample02.html', 'r')

html = fo.read()
# html_str = html.decode('utf-8').encode('GBK')
html_str = html
html_parser = etree.HTMLParser()
tree = etree.parse(io.StringIO(html_str.decode('utf-8')), html_parser)
# print tree.xpath('.//')
print tree.xpath('//@code')

# type(tree.xpath('//div[@id="testid"]/h2/text() | //li[@data]/text()'))
for item in tree.xpath('//div[@id="testid"]/h2/text() | //li[@data]/text()'):#多个匹配条件
    print item.encode('GBK')

# 1. child：选取当前节点的所有子元素
print tree.xpath('//div[@id="testid"]/child::ul/li/text()') #child子节点定位
# print tree.xpath('//div[@id="testid"]/child::ol/text()')
print tree.xpath('//div[@id="testid"]/child::ol/li[@data="two"]')  # [<Element li at 0x2665c08>]
print tree.xpath('//div[@id="testid"]/child::*') #child::*当前节点的所有子元素
#定位某节点下为ol的子节点下的所有节点
print tree.xpath('//div[@id="testid"]/child::ol/child::*/text()')
print tree.xpath('//div[@id="testid"]/ol/child::*/text()')            # 上面两条语句的输出都是  ['1', '2', '3', 'one1', 'two2', 'three3']
print tree.xpath('//div[@id="testid"]/child::*/child::*/text()')

# 2.attribute：选取当前节点的所有属性
print tree.xpath('//div/attribute::id') #attribute定位id属性值
print tree.xpath('//div[@id="testid"]/attribute::*') #定位当前节点的所有属性值

# 3.ancestor：父辈元素 / ancestor-or-self：父辈元素及当前元素
print tree.xpath('//div[@id="testid"]/ancestor::div/@price') #定位父辈div元素的price属性
print tree.xpath('//div[@id="testid"]/ancestor::div/div[@id="good"]/@id') # ['good']
print tree.xpath('//div[@id="testid"]/ancestor::div') #所有父辈div元素
print tree.xpath('//div[@id="testid"]/ancestor-or-self::div') #所有父辈及当前节点div元素

# 4.descendant：后代 / descendant-or-self：后代及当前节点本身,使用方法同上.

# 5. following :选取文档中当前节点的结束标签之后的所有节点
#定位testid之后不包含id属性的div标签下所有的li中第一个li的text属性
print tree.xpath('//div[@id="testid"]/following::div[not(@id)]/.//li[1]/text()')
print tree.xpath('//div[@id="testid"]/following::div[not(@id)]/.//li/text()')           # 上面两行可以显示出 .// 的作用
print tree.xpath('//div[@id="testid"]/following::div[not(@id)]/h3/ul/li[1]/text()')
print tree.xpath('//div[@id="testid"]/following::div[not(@id)]/.//li[1]')
# 6. namespace：选取当前节点的所有命名空间节点
print tree.xpath('//div[@id="testid"]/namespace::*') #选取命名空间节点 ？？？？

# 7. 选取data值为one的父节点的子节点中最后一个节点的值
print type(tree.xpath('//li[@data="one"]/parent::ol/li[last()]/text()'))
print tree.xpath('//li[@data="one"]/parent::ol/li[last()]/text()')
print '=='
print tree.xpath('//li[@data="one"]/parent::ol/li')
# 8. preceding：选取文档中当前节点的开始标签之前的所有节点(需要同时有开始标签和结束标签才是一个完整的节点)
print tree.xpath('//div[@id="testid"]/preceding::div/ul/li[1]/text()')[0]
print tree.xpath('//div[@id="testid"]/preceding::head')
print tree.xpath('//div[@id="testid"]/preceding::body') # 返回空列表[]
print tree.xpath('//div[@id="testid"]/preceding::meta') # [<Element meta at 0x22c9c88>]
print type(tree.xpath('//div[@id="testid"]/preceding::div/ul/li[1]/text()')[0])
# 9. 下面这两条可以看到其顺序是靠近testid节点的优先
print tree.xpath('//div[@id="testid"]/preceding::li[1]/text()')[0]  # 任务
print tree.xpath('//div[@id="testid"]/preceding::li[3]/text()')[0]  # 时间

# 10. 记住只能是同级节点
print tree.xpath('//div[@id="testid"]/preceding-sibling::div/ul/li[2]/text()')[0]
print len(tree.xpath('//div[@id="testid"]/preceding-sibling::div/ul/li[2]/text()'))
print tree.xpath('//div[@id="testid"]/preceding-sibling::li') #这里返回的就是空的了

# 11. 选取带id属性值的div中包含data-h属性的标签的所有属性值
print tree.xpath('//div[@id]/self::div[@data-h]/attribute::*') # ['testid', 'first']
print tree.xpath('//div[@id]/self::div[@data-h]/attribute::data-h')

# 12. 组合：定位id值为testid下的ol下的li属性值data为two的父元素ol的兄弟前节点h2的text值
print tree.xpath('//*[@id="testid"]/ol/li[@data="two"]/parent::ol/preceding-sibling::h2/text()')[0]   # 这里是个小标题

# 13. position 定位
print tree.xpath('//*[@id="testid"]/ol/li[position()=2]/text()')[2]

# 14. 定位所有h2标签中text值为`这里是个小标题`
print tree.xpath(u'//h2[text()="这里是个小标题"]/text()')[0]   # 这里是个小标题

# xpath中的相关函数
# 15 统计
print tree.xpath('count(//li[@data])') #节点统计

# 16 concat：字符串连接
print tree.xpath('concat(//li[@data="one"]/text(),//li[@data="three"]/text())')

# 17 string只能解析匹配到的第一个节点下的值，也就是作用于list时只匹配第一个
print tree.xpath('string(//li)')  # 时间

# 18 解析节点名称,返回第一个匹配的名称
print tree.xpath('local-name(//*[@id="testid"])') #local-name解析节点名称

# 19 contains(string1,string2)：如果 string1 包含 string2，则返回 true，否则返回 false
print tree.xpath('//h3[contains(text(),"uu")]/a/text()')[0]
#使用字符内容来辅助定位 #百度一下 >
#  组合
#匹配带有href属性的a标签的先辈节点中的div，其前一个div节点下ul下li中text属性包含“务”字的节点的值
print tree.xpath(u'//a[@href]/ancestor::div/preceding::div/ul/li[contains(text(),"务")]/text()')[0]   #任务

# 20 not：布尔值（否）
print tree.xpath('count(//li[not(@data)])') #不包含data属性的li标签统计   18.0

# 21 string-length：返回指定字符串的长度
#string-length函数+local-name函数定位节点名长度小于2的元素
print tree.xpath('//*[string-length(local-name())<2]/text()')[0] #百度一下 标签为a

#contains函数+local-name函数定位节点名包含di的元素
print tree.xpath('//div[@id="testid"]/following::div[contains(local-name(),"di")]') # [<Element div at 0x225e108>, <Element div at 0x225e0c8>]

# 22 or：多条件匹配
print tree.xpath('//li[@data="one" or @code="84"]/text()') #or匹配多个条件 ['1', '84']
#也可使用|  ,注意or和|的用法有所不同
print tree.xpath('//li[@data="one"]/text() | //li[@code="84"]/text()')   #|匹配多个条件 ['1', '84']

# 23 position定位+last+div除法，选取中间两个
print tree.xpath('//div[@id="go"]/ul/li[position()=floor(last() div 2+0.5) or position()=ceiling(last() div 2+0.5)]/text()') #['5', '6']

# 24 隔行定位：position+mod取余
# position+取余运算隔行定位
print tree.xpath('//div[@id="go"]/ul/li[position()=((position() mod 2)=0)]/text()')

# 25 starts-with：以。。开始
# starts-with定位属性值code以8开头的li元素
print tree.xpath('//li[starts-with(@code,"8")]/text()')[0]  # 84

# 数值比较
# 25 所有li的code属性小于200的节点
print tree.xpath('//li[@code<200]/text()')   # ['84', '104', '105', '84', '104']

# 25 div：对某两个节点的属性值做除法
print tree.xpath('//div[@id="testid"]/ul/li[3]/@code div //div[@id="testid"]/ul/li[1]/@code')    # 2.65476190476
print tree.xpath('89 div 9')

# 组合：根据节点下的某一节点数量定位
# 选取所有ul下li节点数大于5的ul节点
print tree.xpath('//ul[count(li)>5]/li/text()')  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# 26 将对象还原为字符串
s = tree.xpath('//*[@id="testid"]')[0]  #使用xpath定位一个节点  s <Element div at 0x2b6ffc8>
s2 = etree.tostring(s) #还原这个对象为html字符串 >>> s2
print type(s2)
print type(s2.decode('utf-8'))
h = HTMLParser.HTMLParser()
print h.unescape(s2)  #得到网页内容的html代码时，网页中的中文都会显示成 NCR 字符的形式，可使用HTMLParser的unescape()方法转换 https://www.jianshu.com/p/fb026309867b