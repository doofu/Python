# -*- encoding: gb2312 -*- 
import codecs
import chardet

#===============================================================================
# codingToBytes 将字符串（unicode编码）转为bytes(encoding编码)
# 与str.encode有何区别？
#===============================================================================
def codingToBytes(srcStr, encoding, errors='strict'):
    look = codecs.lookup(encoding)          # 创建displayCoding编码的编码器
    bstr = look.encode(srcStr, errors)      # 用编码器，将字符串转为bytes类型（displayCoding编码）
    return bstr[0]                          # 返回bytes串（displayCoding编码）    

if __name__ == "__main__":
    print(' - ' * 60) 
    
    #  创建gb2312编码器 
    look   =  codecs.lookup( "gb2312" )
    #  创建utf-8编码器 
    look2  =  codecs.lookup( "utf-8" )
    
    # Python3中，所有字符串已是Unicode编码,只能encode为某一个编码类型的字节字符串bytes，而不能decode
    # a： python3内部编码为unicode
    a  =   "Python3中，所有字符串已是Unicode编码。" 
    print('字符串长度：', len(a), a, type(a))
    
    #  把a编码为unicode的字串, 编码为"gb2312"的bytes 
    b  =  look.encode(a)
    #  返回的b[0]是数据（编码为"gb2312"的bytes），b[1]是长度
    print('b.gb2312:', '字符串长度：', b[ 1 ], b[0], type(b[0]), chardet.detect(b[0]))
    # 把a编码为unicode的字串, 编码为"utf-8"的bytes
    b2  =  look2.encode(a)
    #  返回的b2[0]是数据（编码为"utf-8"的bytes），b2[1]是长度
    print('b2.utf-8:', '字符串长度：', b2[ 1 ], b2[0], type(b2[0]), chardet.detect(b2[0]))
    # 直接使用encode()
    b3 = a.encode('gb2312')
    print('b3.gb2312:', '字节数：', len(b3), b3, type(b3), chardet.detect(b3))
    b4 = a.encode('utf-8')
    print('b4.utf-8:', '字节数：', len(b4), b4, type(b4), chardet.detect(b4))
    
    #  按"gb2312"编码，将bytes解码为字符串（unicode编码）
    c  =  look.decode(b[0])
    #  发现不一样的地方了吧？转换回来之后，字符串长度由14变为了7! 现在 的返回的长度才是真正的字数，原来的是字节数 
    print('c.gb2312:', '字节数：', c[ 1 ], c[0], type(c[0]))
    #  虽然上面返回了字数，但并不意味着用len求b2[0]的长度就是7了， 仍然还是14，仅仅是codecs.encode会统计字数 
    print('字符串长度：', len(c[0]))
    
    c2  =  look2.decode(b2[0])
    #  发现不一样的地方了吧？转换回来之后，字符串长度由14变为了7! 现在 的返回的长度才是真正的字数，原来的是字节数 
    print('c2.utf-8:', '字节数：', c2[ 1 ], c2[0], type(c2[0]))
    #  虽然上面返回了字数，但并不意味着用len求b2[0]的长度就是7了， 仍然还是14，仅仅是codecs.encode会统计字数 
    print('字符串长度：', len(c2[0]))
    
    # 直接使用decode()解码
    c3 = b3.decode('gb2312')
    print('c3.gb2312:', '字符串长度：', len(c3), c3, type(c3))
    
    c4 = b4.decode('utf-8')
    print('c4.utf-8:', '字符串长度：', len(c4), c4, type(c4))



