# 运行google play store出现“Device is not Certified by Google”的解决办法
- 概览
设备制造商会与 Google 合作，以证明已安装 Google 应用的 Android 设备安全无虞，且能够正常运行应用。要获得 Play 保护机制认证，设备必须通过 Android 兼容性测试。如果您无法在 Android 设备上添加 Google 帐号，则表示您的 Android 设备软件可能未通过 Android 兼容性测试，或者设备制造商尚未将结果提交给 Google 以获得批准。在这种情况下，您的设备未经 Play 保护机制认证，可能不安全。

- 如果您是想在自己设备上使用自定义 ROM 的用户，请在下方提交您的 Google 服务框架 Android ID（而不是 Settings.Secure.ANDROID_ID 或 SSAID）以注册设备。您可以使用 ADB Shell 命令检索此 ID：
   -   $ adb root

  -   $ adb shell 'sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";"'

  -   https://www.google.com/android/uncertified/
