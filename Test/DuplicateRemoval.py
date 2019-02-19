# coding=utf-8
import json
import copy

from pymongo import MongoClient
conn = MongoClient('127.0.0.1', 27017)
db = conn.apps #数据库名称

global jsonData
jsonData = []

#去重数据
def aggregate(apk_packageName):
    count=0
    for patent_record in db.apkinfo.find({"apk_packageName":apk_packageName}):
        count += 1
 
    while count > 1:
        db.apkinfo.delete_one({"apk_packageName":apk_packageName})
        count -= 1  



def appstore_all():
    
    cursor= db.apkinfo.find()
    
    for row in cursor:
        aggregate(row['apk_packageName'])

if __name__ == '__main__':
    appstore_all()
