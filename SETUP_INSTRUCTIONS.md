# Gourmet Club POS App - APK Build Instructions

## Overview
This document explains how to build the Android APK for the Gourmet Club POS web wrapper app.

## New Package Name
- **Old Package:** com.gourment.ica (conflicting signature)
- **New Package:** `com.gourmetclub.posapp` (unique, no conflicts)

## Signing Certificate Generated
```
Certificate Details:
- Keystore File: gourmet_keystore.jks
- Store Password: GourmetClub@2024
- Key Alias: gourmet_key
- Key Password: GourmetClub@2024
- Validity: 25 years
```

## Build Instructions

### Option 1: Using Android Studio (Recommended)

1. **Install Android Studio**
   - Download from: https://developer.android.com/studio

2. **Create New Project**
   - File → New → New Android Studio Project
   - Choose "Empty Activity"
   - Name: GourmetClubPOS
   - Package name: com.gourmetclub.posapp
   - Minimum API: 21
   - Click Finish

3. **Replace Files**
   - Replace `AndroidManifest.xml` with the provided one
   - Replace `MainActivity.java` in `src/main/java/com/gourmetclub/posapp/`
   - Replace `activity_main.xml` in `res/layout/`
   - Update `build.gradle` with signing config
   - Update `strings.xml`

4. **Add Keystore**
   - Place `gourmet_keystore.jks` in the project root directory

5. **Build APK**
   - Build → Build Bundle(s) / APK(s) → Build APK(s)
   - Wait for build to complete
   - APK will be in: `app/build/outputs/apk/release/`

### Option 2: Using Command Line

```bash
# Build release APK
./gradlew assembleRelease

# APK location
# app/build/outputs/apk/release/app-release.apk
```

## Installation on Device

1. **Enable Unknown Sources**
   - Settings → Security → Unknown Sources (Enable)

2. **Transfer APK**
   - Copy app-release.apk to your device via USB

3. **Install**
   - Open File Manager on device
   - Find and tap the APK
   - Follow installation prompts

4. **Alternative - ADB**
   ```bash
   adb install app/build/outputs/apk/release/app-release.apk
   ```

## Features Included

✅ Web wrapper for https://gourmetclubjordan.com/#/pos/inbox
✅ JavaScript enabled
✅ DOM storage enabled
✅ Camera permission (if needed)
✅ Back button navigation
✅ Internet permission
✅ Unique package name (no conflicts)
✅ New signing certificate
✅ Android 5.0+ support

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "App not installed" | Check package name is unique, permissions enabled |
| Signature conflict | Different package name used: com.gourmetclub.posapp |
| WebView loads blank | Check internet connection, ensure URL is accessible |
| JavaScript not working | Already enabled in code |
| Back button not working | Implemented in MainActivity |

## APK Specifications

- **App Name:** Gourmet Club POS
- **Package:** com.gourmetclub.posapp
- **Min API:** 21 (Android 5.0)
- **Target API:** 34 (Android 14)
- **Version:** 1.0
- **Build Type:** Release (Signed)

## Support

If you encounter issues:
1. Check internet connection
2. Verify URL is accessible: https://gourmetclubjordan.com
3. Ensure all files are in correct locations
4. Check Android version (minimum 5.0)

---
**Generated:** 2024
**Status:** Ready for Build
