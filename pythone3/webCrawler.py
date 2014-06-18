#!/usr/bin/python
#coding: utf-8
'''
Created on 2014年6月18日

@author: user
网络爬虫
'''
import urllib.request
import re

#===============================================================================
# getHtml 取url网址的网页源代码
#===============================================================================
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode()
    
    return(html)
    
#===============================================================================
# getImg 下载网页中符合正则表达式的所有图片
#===============================================================================
def getImg(html):
    # 取到所有图片的url
    reg = r'src="(.*?\.jpg)" width'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg, html)
    
    # 下载所有图片
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jgp' % x)
        x += 1
    
    return imglist
    
html = getHtml('http://python/static/index.html')
print(html)

#getImg(html)

