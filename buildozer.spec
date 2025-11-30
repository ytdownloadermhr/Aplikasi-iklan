[app]
title = AutoSafeAd
package.name = autosafead
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Wajib ada kivmob di sini
requirements = python3,kivy==2.1.0,kivmob,android,jnius

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Konfigurasi Teknis Android & AdMob
android.api = 31
android.minapi = 21
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:19.7.0'
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
