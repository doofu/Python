#!/usr/bin/python
#coding: utf-8
'''
Created on 2014年6月18日

@author: user
网络爬虫
'''
import urllib.request
import re
import io, gzip

#===============================================================================
# getHtml 取url网址的网页源代码
# 参数        url:        网址
#         encode:     网页的编码方式
# 返回         网页的源代码，encode编码的字符串，用于将网页读来的源代码(bytes)转码为python内部格式(unicode编码)
#===============================================================================
def getHtml(url, encode='utf-8'):
    page = urllib.request.urlopen(url)
    html = page.read()      # html为bytes类型，编码为网页的编码方式
    print(html[:6])
    
    # 如果是gzip压缩过后的数据，则用gzip解压缩，然后就正常了
    #gzip解压缩
    if html[:6] == b'\x1f\x8b\x08\x00\x00\x00':
        html = gzip.GzipFile(fileobj = io.BytesIO(html)).read()     # html为bytes类型
    
    html = html.decode(encode)      # 将byte(encode编码)转为str(unicode编码)
    
    return(html)
    
#===============================================================================
# getImg 下载网页中符合正则表达式的所有图片
#===============================================================================
def getImg(html, reg = r'src="(.*?\.jpg)"'):
    # 取到所有图片的url
    #reg = r'src="(.*?\.[jpg,gif])"' # width'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg, html)
        
    # 下载所有图片
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1
    
    return imglist

if __name__ == "__main__": 
    pageCoding = 'utf-8'        # 要访问的网页的编码方式

    #html = getHtml('http://www.sina.com', 'gbk')
    html = getHtml('http://www.baidu.com/', 'utf-8')
    #html = getHtml('http://python/static/index.html', pageCoding)
    
    # 一下语句在windows的command窗口中运行，有时不能被正确执行
    # 因为command窗口是GBK代码显示，在显示前，会自动将unicode代码转为GBK，然而不是所有unicode代码都能正确找到gbk（gbk中字库少），
    # 此时，会在转码时出错
    print(html) #[:8500])
    
    getImg(html)
    


