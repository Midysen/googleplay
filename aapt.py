# -*- coding: utf-8 -*-
import os
from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.apps
my_set = db.apkinfo

#print(my_set.find_one({"apk_packageName":"com.facebook.katana"}))
#db.apkinfo.update({'apk_packageName':"com.facebook.katana"},{'$set' : {'apk_versionName':"4.1.1"}})

#����shell�ű���ʹ��aapt����������apk�ļ��еİ汾��
str=os.popen('./test.sh')
s=str.read()
#print(s.split("\n"))
print(s.split("\n"))

num=0
while num < len(s.split("\n"))-1:
    #print(num)
    versionName=s.split("\n")[num]
    packageName=s.split("\n")[num+1]
    #���ݰ�����ѯ���ݿ⣬���汾�Ų������ݿ�
    db.apkinfo.update({'apk_packageName':'com.facebook.katana'},{'$set' : {'apk_versionName':versionName}})
    print('######')
    print(versionName)
    print(packageName)
    print('******')
    num += 2