# -*- encoding: gb2312 -*- 
import codecs
import chardet

#===============================================================================
# codingToBytes ���ַ�����unicode���룩תΪbytes(encoding����)
# ��str.encode�к�����
#===============================================================================
def codingToBytes(srcStr, encoding, errors='strict'):
    look = codecs.lookup(encoding)          # ����displayCoding����ı�����
    bstr = look.encode(srcStr, errors)      # �ñ����������ַ���תΪbytes���ͣ�displayCoding���룩
    return bstr[0]                          # ����bytes����displayCoding���룩    

if __name__ == "__main__":
    print(' - ' * 60) 
    
    #  ����gb2312������ 
    look   =  codecs.lookup( "gb2312" )
    #  ����utf-8������ 
    look2  =  codecs.lookup( "utf-8" )
    
    # Python3�У������ַ�������Unicode����,ֻ��encodeΪĳһ���������͵��ֽ��ַ���bytes��������decode
    # a�� python3�ڲ�����Ϊunicode
    a  =   "Python3�У������ַ�������Unicode���롣" 
    print('�ַ������ȣ�', len(a), a, type(a))
    
    #  ��a����Ϊunicode���ִ�, ����Ϊ"gb2312"��bytes 
    b  =  look.encode(a)
    #  ���ص�b[0]�����ݣ�����Ϊ"gb2312"��bytes����b[1]�ǳ���
    print('b.gb2312:', '�ַ������ȣ�', b[ 1 ], b[0], type(b[0]), chardet.detect(b[0]))
    # ��a����Ϊunicode���ִ�, ����Ϊ"utf-8"��bytes
    b2  =  look2.encode(a)
    #  ���ص�b2[0]�����ݣ�����Ϊ"utf-8"��bytes����b2[1]�ǳ���
    print('b2.utf-8:', '�ַ������ȣ�', b2[ 1 ], b2[0], type(b2[0]), chardet.detect(b2[0]))
    # ֱ��ʹ��encode()
    b3 = a.encode('gb2312')
    print('b3.gb2312:', '�ֽ�����', len(b3), b3, type(b3), chardet.detect(b3))
    b4 = a.encode('utf-8')
    print('b4.utf-8:', '�ֽ�����', len(b4), b4, type(b4), chardet.detect(b4))
    
    #  ��"gb2312"���룬��bytes����Ϊ�ַ�����unicode���룩
    c  =  look.decode(b[0])
    #  ���ֲ�һ���ĵط��˰ɣ�ת������֮���ַ���������14��Ϊ��7! ���� �ķ��صĳ��Ȳ���������������ԭ�������ֽ��� 
    print('c.gb2312:', '�ֽ�����', c[ 1 ], c[0], type(c[0]))
    #  ��Ȼ���淵������������������ζ����len��b2[0]�ĳ��Ⱦ���7�ˣ� ��Ȼ����14��������codecs.encode��ͳ������ 
    print('�ַ������ȣ�', len(c[0]))
    
    c2  =  look2.decode(b2[0])
    #  ���ֲ�һ���ĵط��˰ɣ�ת������֮���ַ���������14��Ϊ��7! ���� �ķ��صĳ��Ȳ���������������ԭ�������ֽ��� 
    print('c2.utf-8:', '�ֽ�����', c2[ 1 ], c2[0], type(c2[0]))
    #  ��Ȼ���淵������������������ζ����len��b2[0]�ĳ��Ⱦ���7�ˣ� ��Ȼ����14��������codecs.encode��ͳ������ 
    print('�ַ������ȣ�', len(c2[0]))
    
    # ֱ��ʹ��decode()����
    c3 = b3.decode('gb2312')
    print('c3.gb2312:', '�ַ������ȣ�', len(c3), c3, type(c3))
    
    c4 = b4.decode('utf-8')
    print('c4.utf-8:', '�ַ������ȣ�', len(c4), c4, type(c4))



