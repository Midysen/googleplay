#!/bin/bash


dir="./download/"
#for apk in `ls /home/openthos/Downloads/app/*/*.apk`
cp /home/openthos/Downloads/app . -a
for apk in `ls ./app/*/base.apk`
do
    if [ ! -d $dir ]
    then
        mkdir  $dir
    fi
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
