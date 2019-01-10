# coding=utf-8
import json

from pymongo import MongoClient
conn = MongoClient('127.0.0.1', 27017)
db = conn.apps #数据库名称


cursor= db.apkinfo.find()

jsonData = []

taskId=1

for row in cursor:
    if ('apk_versionName' in row) and ('icon' in row ):
        result = {}
        result['taskId'] = taskId
        result['appName'] =  row['apk_name'][0]
        result['packageName'] =  row['apk_packageName']
        result['versionName'] =  row['apk_versionName']
        result['versionCode'] =  row['apk_versionCode']
        result['downloadUrl'] =  row['apk_packageName']+'.apk'
        result['fileSize'] =  row['apk_fileSize']
        result['describle'] =  row['apk_review'][0]
        result['company'] =  row['apk_company']
        result['type'] =  row['apk_category_1']
        result['star'] =  row['apk_star'][0]
        result['iconUrl'] = row['icon']
        taskId = taskId+1
    else:
        continue
        
    print("#############")
    jsonData.append(result)

#print(jsonData)
print("**************************************************#############")
json = json.dumps(jsonData)

#print(json)

data={"result":"200","message":"ok","data":json}

print(data)
fo = open("foo.txt", "w")
fo.write(str(data))
