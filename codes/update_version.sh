#!/bin/sh
adb shell dumpsys package  $1 | grep "versionName"
