# -*- encoding: gb2312 -*- 
import  codecs

print(' - ' * 60) 

#  创建gb2312编码器 
look   =  codecs.lookup( "gb2312" )
#  创建utf-8编码器 
look2  =  codecs.lookup( "utf-8" )

a  =   "-我爱北京-"           # a： 编码为gb2312的字符串
print(len(a), a, type(a))

#  把a编码为内部的unicode, 但为什么方法名为decode呢，我 的理解是把gb2312的字符串解码为unicode 
b  =  look.encode(a)
#  返回的b[0]是数据，b[1]是长度，这个时候的类型是unicode 了 
print('b.gb2312:', b[ 1 ], b[0], type(b[0]))

b2  =  look2.encode(a)
#  返回的b[0]是数据，b[1]是长度，这个时候的类型是unicode 了 
print('b2.utf-8:', b2[ 1 ], b2[0], type(b2[0]))

#  把内部编码的unicode转换为gb2312编码的字符 串，encode方法会返回一个字符串类型 
c  =  look.decode(b[0])
#  发现不一样的地方了吧？转换回来之后，字符串长度由14变为了7! 现在 的返回的长度才是真正的字数，原来的是字节数 
print('c.gb2312:', c[ 1 ], c[0], type(c[0]))
#  虽然上面返回了字数，但并不意味着用len求b2[0]的长度就是7了， 仍然还是14，仅仅是codecs.encode会统计字数 
print(len(c[0]))

c2  =  look2.decode(b2[0])
#  发现不一样的地方了吧？转换回来之后，字符串长度由14变为了7! 现在 的返回的长度才是真正的字数，原来的是字节数 
print('c2.utf-8:', c2[ 1 ], c2[0], type(c2[0]))
#  虽然上面返回了字数，但并不意味着用len求b2[0]的长度就是7了， 仍然还是14，仅仅是codecs.encode会统计字数 
print(len(c2[0]))



