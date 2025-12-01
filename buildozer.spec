[app]

# (str) Title of your application
title = AutoSafeAd

# (str) Package name
package.name = autosafead

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# PENTING: Saya kunci Kivy di versi 2.2.0 agar stabil
requirements = python3,kivy==2.2.0,kivmob,android,jnius,requests

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# PENTING: Wajib ada INTERNET agar iklan muncul
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# --- BAGIAN KRUSIAL (ANTI ERROR) ---
# Menyetujui lisensi otomatis agar build tidak berhenti
android.accept_sdk_license = True
# Menggunakan arsitektur HP modern (64-bit)
android.archs = arm64-v8a

# (str) Android Gradle dependencies
# Library AdMob (Jangan dihapus)
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:19.7.0'

# (str) python-for-android branch to use
p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
