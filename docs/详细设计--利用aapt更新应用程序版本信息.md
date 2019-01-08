# 实现功能
- google play 页面没有无法获得versionName，versionCode等信息，aapt工具通过反编译apk文件，可以获得以上信息

# shell脚本设计：
```
#!/bin/bash
#遍历指定目录下的所有base.apk,此处base.apk文件是从自动下载脚本下载到对应设备的/data/app下获得
for apk in `ls /media/openthos/5FA55FB47D35DC39/apk/*/base.apk`
do
    #截取versionName
    aapt  dump badging $apk | grep versionName | cut -d "'" -f 6
    #截取packageName
    aapt  dump badging $apk | grep versionName | cut -d "'" -f 2
    #截取versionCode
    aapt  dump badging $apk | grep versionName | cut -d "'" -f 4
    #截取fileSize
    ls -l $apk | cut -d ' ' -f 5
done

```
# python脚本设计：
```
#调用shell脚本，使用aapt解析出所有apk文件中的信息
str=os.popen('./aapt.sh')
s=str.read()

num=0
while num < len(s.split("\n"))-1:
    versionName=s.split("\n")[num]
    packageName=s.split("\n")[num+1]
    versionCode=s.split("\n")[num+2]
    fileSize=s.split("\n")[num+3]
    #根据包名查询数据库，将信息插入数据库
    db.apkinfo.update({'apk_packageName':packageName},{'$set' : {'apk_versionName':versionName}})
    db.apkinfo.update({'apk_packageName':packageName},{'$set' : {'apk_versionCode':versionCode}})
    db.apkinfo.update({'apk_packageName':packageName},{'$set' : {'apk_fileSize':fileSize}})
    num += 4

```
