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
import codecs

#===============================================================================
# getHtml 取url网址的网页源代码
# 参数        url:        网址
#         encode:     网页的编码方式
# 返回         网页的源代码，encode编码的字符串
#===============================================================================
def getHtml(url, encode='utf-8'):
    page = urllib.request.urlopen(url)
    html = page.read()      # html为bytes类型
    print(html[:6])
    
    # 如果是gzip压缩过后的数据，则用gzip解压缩，然后就正常了
    #gzip解压缩
    if html[:6] == b'\x1f\x8b\x08\x00\x00\x00':
        html = gzip.GzipFile(fileobj = io.BytesIO(html)).read()     # html为bytes类型
    
    html = html.decode(encode)      # 按encode编码，将byte转为str
    
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

def codeTo(srcStr, encoding, errors='strict'):
    look = codecs.lookup(encoding)     # 创建displayCoding编码的编码器
    bstr = look.encode(srcStr, errors)     # 用编码器，将字符串转为bytes类型（displayCoding编码）
    return bstr[0].decode(encoding)   # 转为字符串（displayCoding编码）    

if __name__ == "__main__": 
    pageCoding = 'utf-8'        # 要访问的网页的编码方式
    displayCoding = 'gbk'     # 显示的编码方式
    #html = getHtml('http://www.sina.com', pageCoding)
    html = getHtml('http://www.baidu.com/', pageCoding)
    #html = getHtml('http://python/static/index.html', pageCoding)
    
    # 如果网页的编码方式与显示的编码方式不同，则需要转码
    print(html[8526], html[8527], html[8528], html[8529], html[8530], html[8531], html[8532], html[8533], html[8534])
    
    if pageCoding != displayCoding:
        print('由%s转为%s编码' % (pageCoding, displayCoding))
        codeTo(html, displayCoding) #, 'replace') #, 'ignore')

    print(html) #[:5000]) ---    
    
    getImg(html, r'src="(.*?\.gif)"')
    


