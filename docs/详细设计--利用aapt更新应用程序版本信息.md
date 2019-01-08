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
