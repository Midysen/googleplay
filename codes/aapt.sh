#!/bin/bash

for apk in `ls /media/openthos/5FA55FB47D35DC39/apk/*/base.apk`
do
    aapt  dump badging $apk | grep versionName | cut -d "'" -f 6
    aapt  dump badging $apk | grep versionName | cut -d "'" -f 2
    aapt  dump badging $apk | grep versionName | cut -d "'" -f 4
    ls -l $apk | cut -d ' ' -f 5
done
