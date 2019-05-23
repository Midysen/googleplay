# coding=utf-8
import os
import subprocess

from pymongo import MongoClient
conn = MongoClient('127.0.0.1', 27017)
collection = conn.apps.apkinfos

list=[]
packageName=[]
def getVersionName():
    for f in list:
        str = f.split(':')
        packageName.append(str)

    count=len(packageName)
    print(count)
    for p in packageName:
        if count >1:
            count-=1
            apkinfo=collection.find_one({"apk_packageName":p[1]})
            if apkinfo is None:
                continue
            else:
                version_db=apkinfo['apk_version']
                v=os.popen('./update_version.sh ' + p[1])
                version=v.read()
                version_pc=version.split('=')[1].split('\n')[0]
                if version_db != version_pc:
                    collection.update({"apk_packageName":p[1]},{'$set':{"update":"true"}})
  

if __name__ == '__main__':
    os.system('adb connect 192.168.0.85')
    list = os.popen('adb shell pm -l').read()
    list = list.split('\n')
    getVersionName()
