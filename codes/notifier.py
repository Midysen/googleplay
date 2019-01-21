#coding = utf-8
import os
import json
import pyinotify
from pymongo import MongoClient
conn = MongoClient('127.0.0.1', 27017)
db = conn.apps #数据库名称

class OnWriteHandler(pyinotify.ProcessEvent):
    """
    def process_IN_CREATE(self, event):
        print("Create file: %s " %  os.path.join(event.path,event.name))
    """
    def process_IN_DELETE(self, event):
        file_path = os.path.join(event.name)
        print("Delete file: " +  file_path + str(file_path)[:-4])
        f = open("all","r")
        fs = f.read()
        #截取出包名
        if str(file_path)[:-4] in fs:
           print(str(file_path)[:-4])
           db.push.delete_one({"packageName":str(file_path)[:-4]})
           
        #更新最新的数据库表push来更新all文件
        data=[]
        for item in db.push.find({},{"_id":0}):
            data.append(item)
        data={"result":"200","message":"ok","data":data}
        fo = open("all", "w")
        fo.write(str(data))
   
def process_IN_MODIFY(self, event):
        print("Modify file: %s " %  os.path.join(event.path,event.name))
        file_path = os.path.join(event.name)
        f = open("all","r")
        fs = f.read()
        if str(file_path)[:-4] not in fs:
            appstore_generate_all(db.apkinfo)
def auto_compile(path='./download/'):
     wm = pyinotify.WatchManager()
     mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY  #监测类型，如果多种用|分开，pyinotify.IN_CREATE | pyinotify.IN_DELETE
     notifier = pyinotify.Notifier(wm, OnWriteHandler())
     wm.add_watch(path, mask,rec=True,auto_add=True)
     print('==&gt; Start monitoring %s (type c^c to exit)' % path)
     while True:
          try:
              notifier.process_events()
              if notifier.check_events():
                  notifier.read_events()
          except KeyboardInterrupt:
              notifier.stop()
              break


    
           

def appstore_generate_all(collection):
    
    cursor= collection.find()
    
    jsonData = []
    
    taskId=2000
    
    for row in cursor:
        
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
            result['type'] =  str(row['apk_category_1'])
            result['star'] =  str(row['apk_star'][0])
            taskId = taskId+1
        else:
            continue
    
        jsonData.append(result)
            
    if jsonData:
        
        data={"result":"200","message":"ok","data":jsonData}
        
        #print(data)
        fo = open("all", "w")
        fo.write(str(data))
        db.push.insert(jsonData)
        
if __name__ == "__main__":
     auto_compile()
