# Android TV Modules & APKs

Automated builds and releases of Android TV apps patched with [ajstrick81/morphe-androidtv-patches](https://github.com/ajstrick81/morphe-androidtv-patches).

This repository generates both **Magisk / KernelSU / APatch Modules (.zip)** and **Standalone Patched APKs (.apk)** for Android TV, Google TV, Fire TV, and Smart TV devices.

---

## 📺 Supported Apps & Patches

| App | Package Name | Patch Highlights | Build Mode |
|---|---|---|---|
| **Disney+** | `com.disney.disneyplus` | Removes mid-roll / pre-roll / pause ads | Module & APK |
| **Prime Video** | `com.amazon.amazonvideo.livingroom` | In-app ad suppression (movies + TV shows, no DNS required) | Module & APK |
| **Netflix** | `com.netflix.ninja` | Native ad strip (pre-roll, mid-roll, pause overlay); cert check bypass | Module & APK |
| **HBO Max** | `com.wbd.hbomax` | Prefer ad-free fallback stream; disables SSAI ads & prerolls | Module & APK |
| **Peacock** | `com.peacocktv.peacockandroid` | Sky SDK ad suppression; disable auto-updates | Module & APK |
| **Tubi** | `com.tubitv` | Ad-free playback for Android TV | Module & APK |
| **ViX** | `com.univision.prendetv` | Suppress Lura linear ad breaks & SSAI overlays | Module & APK |
| **Pluto TV** | `tv.pluto.android` | Removes VOD ads; masks live TV breaks (slate + mute) | Module & APK |
| **Paramount+** | `com.cbs.ott` | Removes VOD pre-roll / mid-roll ads & pause ads | Module & APK |
| **Twitch** | `tv.twitch.android.app` | Android TV Starshot build ad suppression (strips SSAI tags) | Module & APK |
| **ESPN** | `com.espn.score_center` | Suppress VOD ads; masks live SSAI breaks with slate | Module & APK |

---

## 🚀 Installation

### 1. Magisk / KernelSU / APatch Module (.zip)
1. Download the latest `*-module-*.zip` from the [Releases](https://github.com/ikafly144/android-tv-module/releases) page.
2. Open **Magisk / KernelSU / APatch Manager** on your rooted Android TV device.
3. Select **Install from storage** and choose the downloaded zip.
4. Reboot the device.
5. In-place module updates preserve app data (`pm uninstall -k` fallback) and allow downgrades (`-d`).

### 2. Standalone APK (.apk)
For non-rooted Android TV / Google TV / Fire TV sticks:
1. Download the `*.apk` from [Releases](https://github.com/ikafly144/android-tv-module/releases).
2. Transfer or sideload via ADB, Send Files to TV, Downloader, or USB drive.
3. Install the APK directly on your Android TV device.

---

## ⚙️ CI & Automated Updates
- **Automatic Check**: A daily cron workflow checks for upstream patch releases from `ajstrick81/morphe-androidtv-patches` and updated APK versions from APKMirror. If changes are detected, it builds and publishes a new release automatically.
- **Manual Trigger**: You can run `Build Modules` manually via GitHub Actions to build a specific app, APK version, or patch version.

---

## 🙏 Credits & Acknowledgments
- [ajstrick81/morphe-androidtv-patches](https://github.com/ajstrick81/morphe-androidtv-patches)
- [Morphe](https://github.com/MorpheApp)
- [j-hc/revanced-magisk-module](https://github.com/j-hc/revanced-magisk-module)
