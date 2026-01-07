


# macOS Complete Cheat Sheet
### From Beginner to Expert | M1/M2/M3/M4/M5 Compatible

![macOS Logo](https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/kamalsoft/macOS-cheat-sheet/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## 📋 Table of Contents

* [How to Use This Guide](#how-to-use-this-guide)
* [Top 30 Essential Settings (New Users)](#top-30-essential-settings-for-new-mac-users)
* [Opening Terminal - Step by Step](#opening-terminal---step-by-step)
* [Getting Started (Beginners)](#getting-started-beginners)
* [System Information & Hardware](#system-information--hardware)
* [Apple Silicon Chip Comparison](#apple-silicon-chip-comparison)
* [Terminal Command Reference](#terminal-command-reference)
* [System Configuration](#system-configuration)
* [Keyboard Shortcuts (Comprehensive)](#keyboard-shortcuts-comprehensive)
* [Troubleshooting Guide](#troubleshooting-guide)
* [Developer Tools (Mid-Level)](#developer-tools-mid-level)
* [Advanced Configuration (Pro)](#advanced-configuration-pro)
* [Expert-Level Techniques](#expert-level-techniques)
* [Best Resources by Level](#best-resources-by-level)

---
 
## How to Use This Guide

This cheat sheet is organized by skill level. Find your level and start there:

| Level | Description | Start Here |
|-------|-------------|-----------|
| 🟢 **Beginner** | New to Mac, learning basics | [Top 30 Settings](#top-30-essential-settings-for-new-mac-users) |
| 🟡 **Mid-Level** | Comfortable with Mac, want to do more | [Developer Tools](#developer-tools-mid-level) |
| 🟠 **Pro** | Advanced user, customization & automation | [Advanced Configuration](#advanced-configuration-pro) |
| 🔴 **Expert** | System administration, scripting, optimization | [Expert Techniques](#expert-level-techniques) |

**Symbols Used:**
- 🟢 = Beginner friendly
- 🟡 = Mid-level recommended
- 🟠 = Pro users
- 🔴 = Expert only
- ⚠️ = Caution required
- 💡 = Pro tip
- 🍎 = Apple Silicon (M1/M2/M3/M4/M5) specific

[↑ Back to Top](#table-of-contents)

---

## Top 30 Essential Settings for New Mac Users

If you just got a new Mac or did a fresh install, go through this checklist to optimize your experience immediately.

### 🖱️ Trackpad & Mouse
1.  **Tap to Click**: `System Settings` → `Trackpad` → `Point & Click` → Turn on **Tap to click**. (Saves your fingers!)
2.  **Tracking Speed**: `System Settings` → `Trackpad` → Increase **Tracking speed** to Fast.
3.  **Natural Scrolling**: `System Settings` → `Trackpad` → `Scroll & Zoom` → Toggle **Natural scrolling** based on preference.
4.  **Three-Finger Drag**: `System Settings` → `Accessibility` → `Pointer Control` → `Trackpad Options` → Enable **Use trackpad for dragging** → Select **Three Finger Drag**. (Game changer!)
5.  **Right Click**: `System Settings` → `Trackpad` → `Point & Click` → Secondary click → **Click or Tap with Two Fingers**.

### 🖥️ Finder & Desktop
6.  **Show File Extensions**: Open Finder → `Settings` (Cmd+,) → `Advanced` → Check **Show all filename extensions**.
7.  **Show Path Bar**: Open Finder → `View` Menu → **Show Path Bar**.
8.  **Show Status Bar**: Open Finder → `View` Menu → **Show Status Bar**.
9.  **New Window Location**: Finder `Settings` → `General` → New Finder windows show: **Home Directory** (instead of Recents).
10. **Search Scope**: Finder `Settings` → `Advanced` → When performing a search: **Search the Current Folder**.
11. **Clean Up Desktop**: Right-click Desktop → **Use Stacks** (Automatically organizes files).
12. **Finder Sidebar**: Finder `Settings` → `Sidebar` → Check **Movies**, **Music**, **Pictures**, and your **Home** folder.

### ⚓ Dock & Menu Bar
13. **Auto-Hide Dock**: `System Settings` → `Desktop & Dock` → Turn on **Automatically hide and show the Dock**.
14. **Dock Size**: `System Settings` → `Desktop & Dock` → Adjust Size slider to be smaller (more screen real estate).
15. **Magnification**: `System Settings` → `Desktop & Dock` → Turn on **Magnification** (slight effect).
16. **Battery Percentage**: `System Settings` → `Control Center` → Battery → Show Percentage.
17. **Sound in Menu Bar**: `System Settings` → `Control Center` → Sound → **Always Show in Menu Bar**.
18. **Bluetooth in Menu Bar**: `System Settings` → `Control Center` → Bluetooth → **Always Show in Menu Bar**.

### 🛡️ Security & Privacy
19. **FileVault**: `System Settings` → `Privacy & Security` → Turn On **FileVault** (Disk Encryption). ⚠️ **Crucial!**
20. **Firewall**: `System Settings` → `Network` → `Firewall` → Turn On.
21. **Hot Corners**: `System Settings` → `Desktop & Dock` → `Hot Corners` (bottom right) → Set one corner to **Lock Screen**.
22. **Password Immediately**: `System Settings` → `Lock Screen` → Require password after screen saver begins → **Immediately**.

### ⚡ Performance & Power
23. **Optimized Charging**: `System Settings` → `Battery` → Battery Health → Turn on **Optimized Battery Charging**.
24. **Night Shift**: `System Settings` → `Displays` → **Night Shift** → Schedule: Sunset to Sunrise.
25. **Keyboard Repeat**: `System Settings` → `Keyboard` → Key repeat rate → **Fast**; Delay until repeat → **Short**.

### 🌐 Safari & Internet
26. **Show Full URL**: Safari `Settings` → `Advanced` → Check **Show full website address**.
27. **Enable Develop Menu**: Safari `Settings` → `Advanced` → Check **Show Develop menu in menu bar**.
28. **Default Browser**: `System Settings` → `Desktop & Dock` → Default web browser → Select your preference.

### 🛠️ Miscellaneous
29. **Siri**: `System Settings` → `Siri & Spotlight` → Disable if you don't use it to save resources.
30. **Software Updates**: `System Settings` → `General` → `Software Update` → Click `i` → Turn on **Install Security Responses & System Files**.

[↑ Back to Top](#table-of-contents)

---

## Opening Terminal - Step by Step

### Method 1: Using Spotlight Search (Easiest) 🟢

1. **Press** `Command (⌘) + Space` on your keyboard
2. **Type** `terminal`
3. **Press** `Return (Enter)`

### Method 2: Using Finder 🟢

1. **Click** Finder (Smiling Face)
2. **Go** to Applications → Utilities
3. **Double-click** Terminal

[↑ Back to Top](#table-of-contents)

---

## Getting Started (Beginners)

### Apple Silicon (M-Series) Compatibility 🍎

**M1/M2/M3/M4/M5 Macs Are Special!**

Your Mac has a special type of processor (chip) called "Apple Silicon".

| Feature | Intel Macs | Apple Silicon (M1-M5) |
|---------|------------|----------------------|
| **Architecture** | x86_64 | arm64 |
| **Apps** | All native | Native + Rosetta 2 |
| **Performance** | Standard | High Efficiency & Speed ⚡ |

**Which Mac do you have?** 🟢
1. Click  (Apple menu) → "About This Mac"
2. Look at "Chip" or "Processor".

[↑ Back to Top](#table-of-contents)

---

## System Information & Hardware

### Check Your Mac Specifications 🟢

**Terminal Method:** 🟡

```bash
# Basic system information
sw_vers

# Detailed system info
system_profiler SPSoftwareDataType SPHardwareDataType

# Check if Apple Silicon or Intel
uname -m
# arm64 = Apple Silicon (M1-M5) | x86_64 = Intel
```

**Installing Rosetta 2 (for Intel apps):** 🍎

```bash
# Install Rosetta 2 (one time only)
softwareupdate --install-rosetta
```

[↑ Back to Top](#table-of-contents)

---

## Apple Silicon Chip Comparison

Understanding the differences between the M-Series chips will help you understand your Mac's capabilities.

### 📊 Chip Tiers Explained

| Tier | Best For... | Ideal User |
| :--- | :--- | :--- |
| **Base** (M1/M2/M3/M4/M5) | Everyday tasks, office work, light editing, browsing. | Students, Writers, Office Workers |
| **Pro** (M1/M2/M3/M4/M5 Pro) | Heavy multitasking, coding, photo editing, light video. | Developers, Photographers, Creators |
| **Max** (M1/M2/M3/M4/M5 Max) | 3D rendering, 4K/8K video editing, complex compiling. | Video Editors, 3D Artists, Engineers |
| **Ultra** (M1/M2/M3 Ultra) | Extreme workstation tasks, scientific compute. | Studios, Data Scientists |

### 🚀 Generation Comparison

| Generation | Key Features | Performance Leap |
| :--- | :--- | :--- |
| **M1 (2020)** | The Revolution. First SoC for Mac. Incredible battery life. | 3.5x faster CPU than Intel. |
| **M2 (2022)** | Refined architecture. Better GPU, Media Engine added to base. | ~18% faster CPU, 35% faster GPU than M1. |
| **M3 (2023)** | 3nm Process. Hardware Ray Tracing. Dynamic Caching. | ~15-20% faster than M2. Massive GPU leap. |
| **M4 (2024)** | AI Focused. Enhanced Neural Engine. Efficiency boost. | Significant AI/ML performance gains. |
| **M5 (2025/26)** | Next-Gen Architecture. Extreme efficiency & raw power. | The pinnacle of desktop silicon. |

[↑ Back to Top](#table-of-contents)

---

## Terminal Command Reference

### Beginner Terminal Commands 🟢

**Navigation:**

```bash
pwd                 # Print Working Directory (Where am I?)
ls                  # List files
ls -la              # List all files (including hidden)
cd Documents        # Change Directory to Documents
cd ..               # Go back one folder
cd ~                # Go to Home folder
```

**File Operations:**

```bash
touch file.txt      # Create empty file
mkdir NewFolder     # Create new folder
cp file.txt copy.txt # Copy file
mv file.txt NewLoc/ # Move file
rm file.txt         # Delete file (Careful!)
open .              # Open current folder in Finder
```

### Mid-Level Terminal Commands 🟡

**System Management:**

```bash
top                 # Real-time process viewer
killall Safari      # Force close an app
uptime              # How long has Mac been on?
history             # Show command history
```

**Network:**

```bash
ifconfig            # Network interfaces
ping google.com     # Check internet connection
curl ifconfig.me    # Get public IP
```

### Pro Terminal Commands 🟠

**Advanced Operations:**

```bash
# Find files larger than 100MB
find ~ -size +100M

# Watch file changes
tail -f /var/log/system.log

# Disk usage sorted by size
du -sh * | sort -hr

# Symbolic links
ln -s /original/path /link/path
```

[↑ Back to Top](#table-of-contents)

---

## System Configuration

### Finder Configuration 🟢

**Show Hidden Files:** `Cmd + Shift + .`

**Terminal Method:** 🟡
```bash
# Show hidden files
defaults write com.apple.finder AppleShowAllFiles -bool true
killall Finder

# Show path bar
defaults write com.apple.finder ShowPathbar -bool true
```

### Screenshot Configuration 🟡

**Terminal Tweaks:**
```bash
# Change location to Desktop/Screenshots
mkdir ~/Desktop/Screenshots
defaults write com.apple.screencapture location ~/Desktop/Screenshots
killall SystemUIServer

# Remove shadow from screenshots
defaults write com.apple.screencapture disable-shadow -bool true
```

### Dock Configuration 🟡

```bash
# Auto-hide Dock
defaults write com.apple.dock autohide -bool true

# Speed up Dock animation
defaults write com.apple.dock autohide-time-modifier -float 0.5
killall Dock
```

[↑ Back to Top](#table-of-contents)

---

## Keyboard Shortcuts (Comprehensive)

### 🔑 The "Must Know" Basics
| Shortcut | Action |
|----------|--------|
| **⌘ + Space** | **Spotlight Search** (Launch apps, find files, do math) |
| **⌘ + Q** | **Quit** application (Completely closes it) |
| **⌘ + W** | **Close** current window/tab |
| **⌘ + Tab** | **Switch** between open apps |
| **⌘ + `** (Backtick) | Switch between windows of the **same** app |
| **⌘ + Option + Esc** | **Force Quit** menu (Use when app freezes) |
| **⌘ + ,** (Comma) | Open **Settings/Preferences** for current app |
| **⌘ + H** | **Hide** current app |
| **⌘ + M** | **Minimize** window to Dock |

### 📝 Text Editing & Document Control
| Shortcut | Action |
|----------|--------|
| **⌘ + C** | Copy |
| **⌘ + V** | Paste |
| **⌘ + X** | Cut |
| **⌘ + Z** | Undo |
| **⌘ + Shift + Z** | Redo |
| **⌘ + A** | Select All |
| **⌘ + F** | Find / Search in document |
| **Option + Left/Right** | Move cursor by **word** |
| **⌘ + Left/Right** | Move cursor to **start/end of line** |
| **⌘ + Up/Down** | Move cursor to **top/bottom of document** |
| **Shift + Arrows** | Highlight/Select text |
| **Option + Delete** | Delete previous **word** |
| **⌘ + Delete** | Delete entire line (to left of cursor) |

### 📂 Finder & File Management
| Shortcut | Action |
|----------|--------|
| **⌘ + N** | New Finder Window |
| **⌘ + Shift + N** | Create **New Folder** |
| **Return (Enter)** | **Rename** selected file |
| **Spacebar** | **Quick Look** (Preview file without opening) |
| **⌘ + Delete** | Move to **Trash** |
| **⌘ + Shift + Delete** | **Empty Trash** |
| **⌘ + D** | Duplicate file |
| **⌘ + I** | Get Info (Size, type, permissions) |
| **⌘ + Shift + .** | Toggle **Hidden Files** |
| **⌘ + Option + C** | Copy File Path |
| **⌘ + 1 / 2 / 3 / 4** | View as Icon / List / Column / Gallery |

### 📸 Screenshots & Recording
| Shortcut | Action |
|----------|--------|
| **⌘ + Shift + 3** | Capture **Entire Screen** |
| **⌘ + Shift + 4** | Capture **Selected Area** (Drag crosshair) |
| **⌘ + Shift + 4 + Space** | Capture **Specific Window** (Camera icon appears) |
| **⌘ + Shift + 5** | Open **Screenshot/Recording Utility** (Options menu) |
| **Control + (Any above)** | Copy screenshot to **Clipboard** instead of saving to file |

### 🌐 Web Browsing (Safari/Chrome)
| Shortcut | Action |
|----------|--------|
| **⌘ + T** | New Tab |
| **⌘ + Shift + T** | Reopen **Last Closed Tab** (Lifesaver!) |
| **⌘ + L** | Highlight URL/Address Bar |
| **⌘ + R** | Refresh Page |
| **⌘ + + / -** | Zoom In / Out |
| **⌘ + 0** | Reset Zoom |
| **Control + Tab** | Next Tab |
| **Control + Shift + Tab** | Previous Tab |

### 🖥️ System & Window Management
| Shortcut | Action |
|----------|--------|
| **Control + ⌘ + F** | Toggle **Full Screen** |
| **Control + Up Arrow** | **Mission Control** (See all open windows) |
| **Control + Down Arrow** | App Expose (See windows of current app) |
| **Control + Left/Right** | Switch between **Desktops/Spaces** |
| **Fn + Delete** | Forward Delete (Delete character to right) |
| **Control + ⌘ + Q** | **Lock Screen** immediately |
| **⌘ + Shift + ?** | Open **Help** Menu (Search for menu items!) |

[↑ Back to Top](#table-of-contents)

---

## Troubleshooting Guide

### Common Issues & Fixes 🟢

**1. App is Frozen**
- Press `Cmd + Option + Esc` to open Force Quit menu.
- Select the app and click "Force Quit".
- *Terminal way:* `killall AppName`

**2. Mac is Slow**
- Open **Activity Monitor** (Cmd + Space, type "Activity Monitor").
- Check "CPU" and "Memory" tabs to see what's using resources.
- Restart your Mac (clears RAM and caches).

**3. WiFi Issues**
- Toggle WiFi off and on.
- *Terminal reset:* `sudo killall -HUP mDNSResponder` (Flushes DNS).

**4. Disk Full?**
- Check storage:  → System Settings → General → Storage.
- Use `du -sh *` in Terminal to find large folders.

### Safe Mode 🟡
- **Apple Silicon:** Shut down. Press and hold Power button until "Loading startup options" appears. Select disk, hold Shift, click "Continue in Safe Mode".
- **Intel:** Restart and immediately hold Shift.

[↑ Back to Top](#table-of-contents)

---

## Developer Tools (Mid-Level)

### 1. Xcode Command Line Tools 🟡
Essential for development on macOS.
```bash
xcode-select --install
```

### 2. Homebrew (The Missing Package Manager) 🟡
Install software easily from terminal.

**Install Homebrew:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Common Commands:**
```bash
brew install node           # Install Node.js
brew install git            # Install Git
brew install --cask google-chrome  # Install Chrome app
brew update && brew upgrade # Update everything
brew cleanup                # Remove old versions
```

### 3. Git Configuration 🟡
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "nano" # or code, vim
```

### 4. VS Code Setup 🟡
- Install via Brew: `brew install --cask visual-studio-code`
- Enable `code` command: Open VS Code → Cmd+Shift+P → Type "Shell Command: Install 'code' command in PATH".

[↑ Back to Top](#table-of-contents)

---

## Advanced Configuration (Pro)

### Shell Customization (Zsh) 🟠
Your configuration file is at `~/.zshrc`.

**Useful Aliases:**
Add these to your `.zshrc` file:
```bash
# Edit zshrc easily
alias zshconfig="nano ~/.zshrc"
alias reload="source ~/.zshrc"

# Easier navigation
alias ..="cd .."
alias ...="cd ../.."
alias dl="cd ~/Downloads"
alias dt="cd ~/Desktop"

# Better list
alias ll="ls -la"

# Show hidden files in Finder
alias showfiles="defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder"
alias hidefiles="defaults write com.apple.finder AppleShowAllFiles -bool false && killall Finder"
```

### SSH Key Generation 🟠
For GitHub/GitLab authentication:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# Follow prompts. Public key will be in ~/.ssh/id_ed25519.pub
pbcopy < ~/.ssh/id_ed25519.pub # Copies key to clipboard
```

[↑ Back to Top](#table-of-contents)

---

## Expert-Level Techniques

### System Integrity Protection (SIP) 🔴
Protects system files from modification.
- **Check status:** `csrutil status`
- **Disable (Warning!):** Boot into Recovery Mode → Terminal → `csrutil disable`
- **Enable:** Boot into Recovery Mode → Terminal → `csrutil enable`

### Network Analysis 🔴
```bash
# List open network ports
sudo lsof -i -P | grep LISTEN

# Monitor network traffic
sudo tcpdump -i en0

# Check DNS propagation
dig google.com
```

### Process Management 🔴
```bash
# Find process ID (PID) by name
pgrep -f python

# Kill process by PID
kill -9 <PID>

# View process hierarchy
pstree
```

[↑ Back to Top](#table-of-contents)

---

## Best Resources by Level

| Level | Resource | Description |
|-------|----------|-------------|
| 🟢 | [Apple Support](https://support.apple.com/mac) | Official guides |
| 🟡 | [MacRumors Guides](https://www.macrumors.com/guides/) | News and how-tos |
| 🟠 | [Homebrew Docs](https://docs.brew.sh/) | Package manager docs |
| 🔴 | [SS64 macOS Commands](https://ss64.com/osx/) | Complete command reference |
| 🔴 | [Hacker News](https://news.ycombinator.com/) | Tech news & discussion |

---

<div align="center">

**Idea & Concept:** Kamalesh  
**Copyright:** © 2026 Kamalesh. All Rights Reserved.

*Disclaimer: This guide is not affiliated with, endorsed by, or sponsored by Apple Inc. macOS, Mac, and Apple Silicon are trademarks of Apple Inc. The information provided is for educational purposes only. Use at your own risk.*

</div>
