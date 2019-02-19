#爬取google play上的应用信息，存储于数据库
#cd ./apkinfo_v1.1-CN/ 
#scrapy crawl google

if [ $? ]
then
    cd /home/openthos/AppStore/
    echo "success"
    #app信息去重
    python DuplicateRemoval.py
    #下载所有apk
    node down_main_all.js
    if [ $? ]
    then
        #下载所有apk的图标
        python download_img.py
        if [ $? ]
        then
            #根据已经下载的apk文件，解析出openthos应用商店需要的信息
            python aapt.py
            if [ $? ]
            then
                #生成应用商店需要的all文件和game文件
                python aggregate.py
            fi
        fi
    fi
fi
#上传应用商店需要的文件至180服务器
./push.sh
