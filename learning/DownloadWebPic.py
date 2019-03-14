'''
不用这个库了，我晚上用requests + requests-html 重新写一个图片爬虫
'''
'''
This practice is used to:
download pictures on web.
'''

import urllib.request
import ssl
from bs4 import BeautifulSoup

'''
urllib request.urlopen 访问https时 会验证证书。
所以这里引入ssl模块 模拟证书
这里使用取消全局证书验证。因为后面urlretrieve方法也要用到
另一种方式是伪造证书：
context = ssl._create_unverified_context()
web = request.urlopen(url,context=context)
'''
ssl._create_default_https_context = ssl._create_unverified_context 
web = request.urlopen("https://tieba.baidu.com/p/4961133068")
html = web.read() #读到整个页面的html code

soup = BeautifulSoup(html,'html.parser')
imgtag = soup.findAll('img', _class='BDE_Image') #找到img class是BDE_Image 的tag

i = 0

for img in imgtag:
    imgurl = img.get('src') #得到图片link
    imgfile = request.urlretrieve(imgurl, filename='眠狼%d.jpg'%i)
    i = i+1
    

