1、进入apkinfo_v1.1-CN 目录下，运行 stracpy crawl google， 首先抓取google play上应用程序的信息
2、运行 login_all.py , 完成自动登录下载apk
3、拷贝对应搭载openthos系统的设备下/data/app目录下的所有已经安装的应用对应的apk文件所在的目录
4、运行aapt.py，根据apk文件得到版本等信息，更新数据库;调用aapt.sh脚本，实现以包名重命名所有base.apk文件，并拷贝到download目录下
5、运行download_img.py 文件，根据包名下载所有应用程序的图标，下载到image目录下，并更新数据库，添加字段icon
6、运行aggregate.py脚本，去除重名的应用程序信息，并按照应用商店要求，生成all文件
7、运行notifier.py,实时监测download目录下apk文件的变化，如果是apk文件删除，则从push表删除apk的信息，并更新all文件；如果添加apk文件，则更新push表，并更新all文件
