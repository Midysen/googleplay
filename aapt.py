import os

#����shell�ű���ʹ��aapt����������apk�ļ��еİ汾��
str=os.popen('./test.sh')
s=str.read()
print(s.split("\n"))
print(s.split("'"))
#ss=''.join(s.split("'"))
#print(ss.split("\n"))

num=0
while num < len(s.split("\n"))-1:
    print(num)
    versionName=s.split("\n")[num]
    print(versionName)
    print('###')
    num += 1
