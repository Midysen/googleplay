# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
import socket
import urllib
import os
from pymongo import MongoClient
conn = MongoClient('127.0.0.1', 27017)
db = conn.apps #数据库名称

#显示下载进度
def schedule(a,b,c):
    #a:已下载的数据块 b:数据块的大小 c:远程文件的大小
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)
 
def get_packageNames():
     #从数据库中获得所有包名称
    packageNames=db.apkinfo.find({},{"apk_packageName":1,"_id":0})
    news = []
    for each in packageNames:
        print(each)
        if 'apk_packageName' in each:
            news.append(each['apk_packageName'])

    news_items = []
    for item in news:
        if item not in news_items:
            news_items.append(item)
    #print(news_items)
    return news

def download_icon():
    packages = get_packageNames()
    icons = []
    icon_urls = {}
    for each in packages:
        cursor=db.apkinfo.find_one({"apk_packageName":each})
        #if ('apk_icon' in cursor) and ('icon' not in cursor) :
        if ('apk_icon' in cursor):
            icon_urls={each:cursor['apk_icon'][0]}
            icons.append(icon_urls)
        else:
            continue
    
    return icons
        

def get_images():
    images_list = []
    rootdir='image/'
    if not os.path.exists(rootdir):
        os.mkdir(rootdir)
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isfile(path) and os.path.basename(path).endswith(".png"):
            images_list.append(path)
    return images_list
    """
    str=os.popen('./img.sh')
    s=str.read()
    images=[]
    num=0
    while num < len(s.split("\n"))-1:
        images.append(s.split("\n")[num])
        num = num+1
    return images
    """

if __name__ == '__main__':
    packages = get_packageNames()
    icons_url=download_icon()
    socket.setdefaulttimeout(20)
    for url in icons_url:
        for each in packages:
            if each in url:
                #url=url[0]
                print(url[each])
                uu=url[each][:-3]
             
                images=get_images()
                #appstore解析显示需要icon字段 
                target = "icon/" + each + ".png"
                db.apkinfo.update({'apk_packageName':each},{'$set' : {'icon':target}})
                #下载的png图标统一放到image目录下 
                target = "image/" + each + ".png"
                if target not in images:
                    try:
                        urlretrieve(uu,target,schedule)
                    except urllib.error.URLError:
                        count = 1
                        while count <= 3:
                            try:
                                urlretrieve(uu,target,schedule)                                               
                                break
                            except urllib.error.URLError:
                                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                                print(err_info)
                                count += 1
                        if count > 3:
                            print("downloading picture fialed!")
                else:
                    continue
        
