import os

#调用shell脚本，使用aapt解析出所有apk文件中的版本号
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
