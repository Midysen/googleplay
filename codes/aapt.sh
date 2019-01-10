#!/bin/bash

for apk in `ls /media/openthos/5FA55FB47D35DC39/apk/*/base.apk`
do
    a=`aapt dump badging $apk | grep versionName | cut -d "'" -f 2`.apk
    cp $apk ./download/$a
    aapt  dump badging ./download/$a | grep versionName | cut -d "'" -f 6
    aapt  dump badging ./download/$a | grep versionName | cut -d "'" -f 2
    aapt  dump badging ./download/$a | grep versionName | cut -d "'" -f 4
    ls -l ./download/$a | cut -d ' ' -f 5
done
