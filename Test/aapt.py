# -*- coding: utf-8 -*-
import os

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.apps
my_set = db.apkinfo

#print(my_set.find_one({"apk_packageName":"com.facebook.katana"}))
#db.apkinfo.update({'apk_packageName':"com.facebook.katana"},{'$set' : {'apk_versionName':"4.1.1"}})

#µ÷ÓÃshell½Å±¾£¬Ê¹ÓÃaapt½âÎö³öËùÓÐapkÎÄ¼þÖÐµÄ°æ±¾ºÅ
str=os.popen('./aapt.sh')
s=str.read()
#print(s.split("\n"))
print(s.split("\n"))

num=0
while num < len(s.split("\n"))-1:
    #print(num)
    versionName=s.split("\n")[num]
    packageName=s.split("\n")[num+1]
    versionCode=s.split("\n")[num+2]
    fileSize=s.split("\n")[num+3]
    #根据包名更新数据库
    db.apkinfo.update({'apk_packageName':packageName},{'$set' : {'apk_versionName':versionName}})
    db.apkinfo.update({'apk_packageName':packageName},{'$set' : {'apk_versionCode':versionCode}})
    db.apkinfo.update({'apk_packageName':packageName},{'$set' : {'apk_fileSize':fileSize}})
    print('######')
    print(versionName)
    print('######')
    print(packageName)
    print('######')
    print(versionCode)
    print('######')
    print(fileSize)
    print('******')
    num += 4
