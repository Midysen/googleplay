#!/bin/bash

for apk in `ls ~/*.apk`
do
    aapt  dump badging $apk | grep versionName | cut -d "'" -f 6

done

#aapt  dump badging ~/weixin_1360.apk | grep versionName | cut -d "'" -f 6
#aapt  dump badging ~/weixin_1360.apk | grep versionName
