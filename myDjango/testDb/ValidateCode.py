#!/usr/bin/env python
#coding=utf-8
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
import os

class ValidateCode:
    charset = ''                    #随机因子
    codelen = 4                     # 验证码长度
    width = 90  #130                # 宽度
    height = 30 #50                 # 高度
    font = ''                       # 指定的字体
    fontsize = 18                   # 指定字体大小
    mode = "RGB"

    code = ''                       # 验证码
    img = ''                        # 图形资源句柄
    #fontcolor = (0, 0, 0)           # 指定字体颜色
    bg_color = (255, 255, 255)

    #构造方法初始化
    def __init__(self, charset = 'abcdefghkmnprstuvwxyzABCDEFGHKMNPRSTUVWXYZ23456789',    #随机因子
                        codelen = 4,
                        width = 90,
                        height = 30,
                        font = '\\font\\elephant.ttf',
                        fontsize = 18,
                        mode = 'RGB'):
        self.charset = charset
        self.codelen = codelen
        self.width = width
        self.height = height
        # 获得字体文件elephant.ttf的绝对路径
        self.font = os.path.dirname(__file__) + font
        self.fontsize = fontsize
        self.mode = mode

    #生成随机码
    def createCode(self):
        for i in range(self.codelen):
            self.code += self.charset[random.randrange(len(self.charset))]

    #生成背景
    def createBg(self):
        bg_color = (random.randrange(157, 255), random.randrange(157, 255), random.randrange(157, 255))
        self.img = Image.new(self.mode, (self.width, self.height), bg_color) # 创建图形
        self.draw = ImageDraw.Draw(self.img) # 创建画笔

    #生成文字
    def createFont(self):
        #c_chars = random.sample(self.code, self.codelen)
        #strs = ' %s ' % ' '.join(c_chars) # 每个字符前后以空格隔开
        font = ImageFont.truetype(self.font, self.fontsize)
        self.fontcolor = (random.randrange(0, 156), random.randrange(0, 156), random.randrange(0, 156))
        
        i = 0
        x = (self.width - 10) / self.codelen
        for c in self.code:
        #self.draw.text(((self.width - font_width) / 3, (self.height - font_height) / 3),self.code, font=font, fill=self.fontcolor)
            fontcolor = (random.randrange(0, 156), random.randrange(0, 156), random.randrange(0, 156))
            font_width, font_height = font.getsize(c)
            self.draw.text((x * i + random.randrange(1,5), (self.height - font_height) / 3), c, font=font, fill=fontcolor)
            i += 1

    def createLine(self):
        # 绘制干扰线条
        for i in range(6):
            color = (random.randrange(0, 156), random.randrange(0, 156), random.randrange(0, 156))
            begin = (random.randrange(0, self.width),random.randrange(0, self.height))
            end = (random.randrange(0, self.width),random.randrange(0, self.height))
            self.draw.line([begin, end], fill=color)

    def createSnow(self): 
        # 绘制干扰雪花
        for i in range(100):
            font = ImageFont.truetype(self.font, random.randrange(1, 15))
            color = (random.randrange(200, 255), random.randrange(200, 255), random.randrange(200, 255))
            self.draw.text((random.randrange(0,self.width), random.randrange(0,self.height)), '*', font=font, fill=color)
    
    def createPoints(self):
        # 绘制干扰点
        point_chance = 2    # 干扰点出现的概率，大小范围[0, 100]
        chance = min(100, max(0, int(point_chance))) # 大小限制在[0, 100]
 
        for w in range(self.width):
            for h in range(self.height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    color = (random.randrange(0, 55), random.randrange(0, 55), random.randrange(0, 55))
                    self.draw.point((w, h), fill=color) #(0, 0, 0))
                    
    def warpPic(self):
        # 图形扭曲参数
        params = [1 - float(random.randint(1, 2)) / 100,
            0,
            0,
            0,
            1 - float(random.randint(1, 10)) / 100,
            float(random.randint(1, 2)) / 500,
            0.001,
            float(random.randint(1, 2)) / 500
            ]
        self.img = self.img.transform((self.width, self.height), Image.PERSPECTIVE, params) # 创建扭曲

        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 滤镜，边界加强（阈值更大）
 
    # 将图像保存到文件中
    def saveToFile(self, fileName):
        self.img.save(fileName, "GIF")
        
    def toPicBuffer(self):
        # 如果每次生成验证码，都要先保存生成的图片，再显示到页面。这么做让人太不能接受了。
        # 这个时候，我们需要使用python内置的io模块（python2为StringIO或cStringIO模块)，
        # 它有着类似file对象的行为，但是它操作的是内存文件。
        mstream = io.BytesIO()
        self.img.save(mstream, "GIF") 
        
        return mstream.getvalue()

    #获取验证码
    def getCode(self):
#        return self.code.lower()
        return self.code        # 区分大小写

    def createCheckNum(self):
        self.createCode()
        
        self.createBg()
        self.createLine()
#        #self.createSnow()
        self.createPoints()
        self.createFont()
        self.warpPic()
        
        return self.img