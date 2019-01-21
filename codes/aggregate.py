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


def appstore_generate_category():
    global jsonData
    json_game =[]
    for category in jsonData:
        if category['type'] == "游戏":
            print(category)
            json_game.append(category)
    #json_game_data = json.dumps(json_game)
    data=[]
    data.append({"type":"全部","whole":"所有","data":json_game})
    
    data={"result":"200","message":"ok","data":data}
    fo = open("game", "w")
    fo.write(str(data))


def appstore_generate_all():
    
    cursor= db.apkinfo.find()
    
    global jsonData
    
    taskId=1
    
    for row in cursor:
        aggregate(row['apk_packageName'])
        if ('apk_versionName' in row) and ('icon' in row ):
            result = {}
            result['taskId'] = str(taskId)
            result['appName'] =  str(row['apk_name'][0])
            result['packageName'] =  str(row['apk_packageName'])
            result['versionName'] =  str(row['apk_versionName'])
            result['versionCode'] =  str(row['apk_versionCode'])
            result['downloadUrl'] =  "download/" + row['apk_packageName']+'.apk'
            result['iconUrl'] = row['icon']
            result['fileSize'] =  str(row['apk_fileSize'])
            result['describle'] =  str(row['apk_review'][0])
            result['company'] =  str(row['apk_company'])
            if row['apk_category_1'].startswith('GAME'):
                result['type'] =  "游戏"
            if row['apk_category_1'].startswith('MUSIC'):
                result['type'] =  "图像影音"
            if row['apk_category_1'].startswith('PRODUCTIVITY'):
                result['type'] =  "系统工具"
            if row['apk_category_1'].startswith('DATING'):
                result['type'] =  "网络社交"
            else:
                result['type'] =  str(row['apk_category_1'])
            result['star'] =  str(row['apk_star'][0])
            
            taskId = taskId+1
        else:
            continue
    
        jsonData.append(result)
        print(jsonData)
    if jsonData:
    
        #jsons = json.dumps(jsonData)
        #print(jsons)
        
        data={"result":"200","message":"ok","data":jsonData}
        
        #print(data)
        fo = open("all", "w")
        fo.write(str(data))
        #fo.write(jsons)
        json_all = copy.deepcopy(jsonData)
        db.push.insert(json_all)
    else:
        print("no data in jsondata")

if __name__ == '__main__':
    appstore_generate_all()
    appstore_generate_category()
