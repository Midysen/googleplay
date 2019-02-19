#!/bin/bash

#for apk in `ls /home/openthos/Downloads/app/*/*.apk`
for apk in `ls /media/openthos/*/apk/*/base.apk`
do
    a=`aapt dump badging $apk | grep versionName | cut -d "'" -f 2`.apk
    cp $apk ./download/$a
    #versionName
    aapt  dump badging ./download/$a | grep versionName | cut -d "'" -f 6
    #packageName
    aapt  dump badging ./download/$a | grep versionName | cut -d "'" -f 2
    #versionCode
    aapt  dump badging ./download/$a | grep versionName | cut -d "'" -f 4
    ls -l ./download/$a | cut -d ' ' -f 5
done
