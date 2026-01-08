# macOS Mastered

### From Beginner to Expert | M1/M2/M3/M4/M5 Compatible

![macOS Logo](https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/kamalsoft/macOS-cheat-sheet/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--01--08-blue.svg)](https://github.com/kamalsoft/macOS-cheat-sheet/commits/main)

- --

<div class="quick-nav-sidebar">
  <a href="#top-30-essential-settings" class="quick-nav-item" title="Settings">⚙️</a>
  <a href="#opening-terminal-step-by-step" class="quick-nav-item" title="Terminal">💻</a>
  <a href="#keyboard-shortcuts-comprehensive" class="quick-nav-item" title="Shortcuts">⌨️</a>
  <a href="#troubleshooting-guide" class="quick-nav-item" title="Troubleshooting">🚑</a>
  <a href="#developer-tools-mid-level" class="quick-nav-item" title="Developer">🛠️</a>
  <a href="#2-homebrew-the-missing-package-manager" class="quick-nav-item" title="Homebrew">🍺</a>
  <a href="#virtualization" class="quick-nav-item" title="Virtualization">🖥️</a>
</div>


## 📋 Table of Contents

  * [From Beginner to Expert | M1/M2/M3/M4/M5 Compatible](#from-beginner-to-expert-m1m2m3m4m5-compatible)
* [🆕 New & Updated](#new-updated)
* [How to Use This Guide](#how-to-use-this-guide)
* [Beginner: Essentials](#beginner-essentials)
  * [🚀 Top 30 Essential Settings](#top-30-essential-settings)
* [Opening Terminal - Step by Step](#opening-terminal-step-by-step)
  * [Method 1: Using Spotlight Search (Easiest) 🟢](#method-1-using-spotlight-search-easiest)
  * [Method 2: Using Finder 🟢](#method-2-using-finder)
* [Getting Started (Beginners)](#getting-started-beginners)
  * [Apple Silicon (M-Series) Compatibility 🍎](#apple-silicon-m-series-compatibility)
* [System Information & Hardware](#system-information-hardware)
  * [Check Your Mac Specifications 🟢](#check-your-mac-specifications)
* [Apple Silicon Chip Comparison](#apple-silicon-chip-comparison)
  * [📊 Chip Tiers Explained](#chip-tiers-explained)
  * [🚀 Generation Comparison](#generation-comparison)
* [Terminal Command Reference](#terminal-command-reference)
  * [Beginner Terminal Commands 🟢](#beginner-terminal-commands)
  * [Mid-Level Terminal Commands 🟡](#mid-level-terminal-commands)
  * [Pro Terminal Commands 🟠](#pro-terminal-commands)
* [System Configuration](#system-configuration)
  * [Finder Configuration 🟢](#finder-configuration)
  * [Screenshot Configuration 🟡](#screenshot-configuration)
  * [Dock Configuration 🟡](#dock-configuration)
* [Window Management Apps](#window-management-apps)
  * [1. Rectangle (Free & Open Source) 🟢](#1-rectangle-free-open-source)
  * [2. Magnet (Paid) 🟢](#2-magnet-paid)
* [Menu Bar Apps](#menu-bar-apps)
  * [1. Hidden Bar (Free) 🟢](#1-hidden-bar-free)
  * [2. Ice (Free) 🟢](#2-ice-free)
  * [3. Bartender (Paid) 🟢](#3-bartender-paid)
* [Productivity Apps](#productivity-apps)
  * [1. Raycast (Free for Personal Use) 🟢](#1-raycast-free-for-personal-use)
  * [2. Alfred (Freemium) 🟡](#2-alfred-freemium)
* [Terminal Themes](#terminal-themes)
  * [1. Oh My Zsh 🟡](#1-oh-my-zsh)
  * [2. Powerlevel10k Theme 🟠](#2-powerlevel10k-theme)
* [Backup Strategies](#backup-strategies)
  * [1. Time Machine (Local) 🟢](#1-time-machine-local)
  * [2. Cloud Backup (Off-site) 🟡](#2-cloud-backup-off-site)
* [Keyboard Shortcuts (Comprehensive)](#keyboard-shortcuts-comprehensive)
  * [🔑 The "Must Know" Basics](#the-must-know-basics)
  * [📝 Text Editing & Document Control](#text-editing-document-control)
  * [📂 Finder & File Management](#finder-file-management)
  * [📸 Screenshots & Recording](#screenshots-recording)
  * [🌐 Web Browsing (Safari/Chrome)](#web-browsing-safarichrome)
  * [🖥️ System & Window Management](#system-window-management)
* [Troubleshooting Guide](#troubleshooting-guide)
  * [Common Issues & Fixes 🟢](#common-issues-fixes)
  * [Safe Mode 🟡](#safe-mode)
* [Developer Tools (Mid-Level)](#developer-tools-mid-level)
  * [1. Xcode Command Line Tools 🟡](#1-xcode-command-line-tools)
  * [2. Homebrew (The Missing Package Manager) 🟡](#2-homebrew-the-missing-package-manager)
  * [3. Git Configuration 🟡](#3-git-configuration)
  * [4. VS Code Setup 🟡](#4-vs-code-setup)
  * [5. Containerization (Docker / OrbStack) 🟡](#5-containerization-docker-orbstack)
* [Homebrew Essentials](#homebrew-essentials)
  * [1. tldr (Too Long; Didn't Read) 🟢](#1-tldr-too-long-didnt-read)
  * [2. htop / btop 🟡](#2-htop-btop)
  * [3. ffmpeg 🔴](#3-ffmpeg)
  * [4. bat 🟢](#4-bat)
* [Virtualization](#virtualization)
  * [1. UTM (Free / Open Source) 🟢](#1-utm-free-open-source)
  * [2. VMware Fusion Pro (Free for Personal Use) 🟡](#2-vmware-fusion-pro-free-for-personal-use)
  * [3. Parallels Desktop (Paid) 🟢](#3-parallels-desktop-paid)
* [Gaming on Mac](#gaming-on-mac)
  * [1. Whisky (Free / Open Source) 🟢](#1-whisky-free-open-source)
  * [2. Game Porting Toolkit (GPTK) 🔴](#2-game-porting-toolkit-gptk)
* [Creative Tools](#creative-tools)
  * [1. DaVinci Resolve (Free / Paid) 🟠](#1-davinci-resolve-free-paid)
  * [2. Blender (Free & Open Source) 🟠](#2-blender-free-open-source)
  * [3. OBS Studio (Free & Open Source) 🟡](#3-obs-studio-free-open-source)
* [Design Tools](#design-tools)
  * [1. Figma (Free / Paid) 🟢](#1-figma-free-paid)
  * [2. Sketch (Paid) 🟠](#2-sketch-paid)
  * [3. Affinity Designer (Paid) 🟢](#3-affinity-designer-paid)
* [Audio Tools](#audio-tools)
  * [1. Loopback (Paid) 🟠](#1-loopback-paid)
  * [2. Audio Hijack (Paid) 🟠](#2-audio-hijack-paid)
* [Music Production](#music-production)
  * [1. Logic Pro (Paid) 🟠](#1-logic-pro-paid)
  * [2. GarageBand (Free) 🟢](#2-garageband-free)
* [Quick Look Plugins](#quick-look-plugins)
  * [1. Syntax Highlight (Free) 🟢](#1-syntax-highlight-free)
  * [2. QLVideo (Free) 🟢](#2-qlvideo-free)
  * [3. QLMarkdown (Free) 🟢](#3-qlmarkdown-free)
* [Advanced Configuration (Pro)](#advanced-configuration-pro)
  * [Shell Customization (Zsh) 🟠](#shell-customization-zsh)
  * [SSH Key Generation 🟠](#ssh-key-generation)
* [Privacy & Security Deep Dive](#privacy-security-deep-dive)
  * [1. Outbound Firewalls 🟠](#1-outbound-firewalls)
  * [2. Malware Monitoring 🟠](#2-malware-monitoring)
* [Maintenance & Cleaning](#maintenance-cleaning)
  * [1. OnyX (Free) 🟠](#1-onyx-free)
  * [2. DaisyDisk (Paid) 🟢](#2-daisydisk-paid)
  * [3. AppCleaner (Free) 🟢](#3-appcleaner-free)
  * [4. Disk Space Analyzer (Terminal) 🟠](#4-disk-space-analyzer-terminal)
* [Networking Tools](#networking-tools)
  * [1. Wireshark (Free / Open Source) 🔴](#1-wireshark-free-open-source)
  * [2. Little Snitch (Paid) 🟠](#2-little-snitch-paid)
  * [3. Network Speed Test](#3-network-speed-test)
* [Remote Access](#remote-access)
  * [1. SSH (Secure Shell) 🟠](#1-ssh-secure-shell)
  * [2. Screen Sharing (VNC) 🟢](#2-screen-sharing-vnc)
  * [3. Microsoft Remote Desktop (Free) 🟡](#3-microsoft-remote-desktop-free)
* [File Management](#file-management)
  * [1. Commander One (Freemium) 🟡](#1-commander-one-freemium)
  * [2. ForkLift (Paid) 🟠](#2-forklift-paid)
* [System Monitoring](#system-monitoring)
  * [1. Stats (Free & Open Source) 🟢](#1-stats-free-open-source)
  * [2. iStat Menus (Paid) 🟢](#2-istat-menus-paid)
  * [3. Activity Monitor (Built-in) 🟢](#3-activity-monitor-built-in)
* [Browser Extensions](#browser-extensions)
  * [1. uBlock Origin (Free / Open Source) 🟢](#1-ublock-origin-free-open-source)
  * [2. 1Password (Paid) 🟢](#2-1password-paid)
* [Communication Apps](#communication-apps)
  * [1. Slack (Freemium) 🟢](#1-slack-freemium)
  * [2. Discord (Free) 🟢](#2-discord-free)
  * [3. Zoom (Free / Paid) 🟢](#3-zoom-free-paid)
* [Email Clients](#email-clients)
  * [1. Spark (Freemium) 🟢](#1-spark-freemium)
  * [2. Mimestream (Paid) 🟢](#2-mimestream-paid)
  * [3. Apple Mail (Built-in) 🟢](#3-apple-mail-built-in)
* [Calendar & Task Apps](#calendar-task-apps)
  * [1. Fantastical (Freemium) 🟢](#1-fantastical-freemium)
  * [2. Things 3 (Paid) 🟢](#2-things-3-paid)
* [Finance & Budgeting](#finance-budgeting)
  * [1. YNAB (You Need A Budget) (Paid) 🟢](#1-ynab-you-need-a-budget-paid)
  * [2. Banktivity (Paid) 🟠](#2-banktivity-paid)
* [Database Tools](#database-tools)
  * [1. TablePlus (Freemium) 🟡](#1-tableplus-freemium)
  * [2. DBngin (Free) 🟢](#2-dbngin-free)
* [Local Development](#local-development)
  * [1. Laravel Herd (Free / Pro) 🟢](#1-laravel-herd-free-pro)
  * [2. MAMP (Free / Pro) 🟡](#2-mamp-free-pro)
  * [3. XAMPP (Free) 🟡](#3-xampp-free)
* [Markdown Editors](#markdown-editors)
  * [1. Obsidian (Free) 🟢](#1-obsidian-free)
  * [2. Bear (Freemium) 🟢](#2-bear-freemium)
  * [3. Typora (Paid) 🟢](#3-typora-paid)
* [Writing Tools](#writing-tools)
  * [1. Scrivener (Paid) 🟠](#1-scrivener-paid)
  * [2. Ulysses (Paid) 🟢](#2-ulysses-paid)
* [Education & Research](#education-research)
  * [1. Zotero (Free & Open Source) 🟢](#1-zotero-free-open-source)
  * [2. Anki (Free & Open Source) 🟢](#2-anki-free-open-source)
* [Mind Mapping](#mind-mapping)
  * [1. MindNode (Freemium) 🟢](#1-mindnode-freemium)
  * [2. XMind (Freemium) 🟡](#2-xmind-freemium)
* [Utilities](#utilities)
  * [1. Amphetamine (Free) 🟢](#1-amphetamine-free)
  * [2. The Unarchiver (Free) 🟢](#2-the-unarchiver-free)
  * [3. CheatSheet (Free) 🟢](#3-cheatsheet-free)
* [Clipboard Managers](#clipboard-managers)
  * [1. Maccy (Free / Open Source) 🟢](#1-maccy-free-open-source)
  * [2. Paste (Paid) 🟢](#2-paste-paid)
* [Automation](#automation)
  * [1. Shortcuts (Built-in) 🟢](#1-shortcuts-built-in)
  * [2. Automator (Built-in) 🟡](#2-automator-built-in)
* [Expert-Level Techniques](#expert-level-techniques)
  * [System Integrity Protection (SIP) 🔴](#system-integrity-protection-sip)
  * [Network Analysis 🔴](#network-analysis)
  * [Process Management 🔴](#process-management)
* [👥 Contributors](#contributors)
* [Best Resources by Level](#best-resources-by-level)

## 🆕 New & Updated

- **2026-01-08**: Refactor documentation updates and enhance slug generation for better compatibility
- **2026-01-08**: Update documentation
- **2026-01-08**: Update documentation
- **2026-01-08**: Update documentation
- **2026-01-08**: Add Contributors section and Last Updated badge to documentation; update sitemap and fix broken link handling

## How to Use This Guide

This guide is organized by skill level. Find your level and start there:

| Level | Description | Start Here |
|-------|-------------|-----------|
| 🟢 **Beginner** | New to Mac, learning basics | [Top 30 Settings](#top-30-essential-settings) |
| 🟡 **Mid-Level** | Comfortable with Mac, want to do more | [Developer Tools](#developer-tools-mid-level) |
| 🟠 **Pro** | Advanced user, customization & automation | [Advanced Configuration](#advanced-configuration-pro) |
| 🔴 **Expert** | System administration, scripting, optimization | [Expert Techniques](#expert-level-techniques) |

* *Symbols Used:**
- 🟢 = Beginner friendly
- 🟡 = Mid-level recommended
- 🟠 = Pro users
- 🔴 = Expert only
- ⚠️ = Caution required
- 💡 = Pro tip
- 🍎 = Apple Silicon (M1/M2/M3/M4/M5) specific

[↑ Back to Top](#table-of-contents)

- --


### 🔗 Related Topics

- Gaming on Mac
- Virtualization
- Getting Started (Beginners)

## Beginner: Essentials

### 🚀 Top 30 Essential Settings

Optimize your experience immediately after a fresh install.

#### 🖱️ Trackpad & Mouse
<table class="shortcuts-table">
  <thead>
    <tr><th>Setting</th><th>Path</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td>Tap to Click</td><td><code>Trackpad</code> → <code>Point & Click</code></td><td>Turn on Tap to click</td></tr>
    <tr><td>Tracking Speed</td><td><code>Trackpad</code></td><td>Increase to Fast</td></tr>
    <tr><td>Natural Scrolling</td><td><code>Trackpad</code> → <code>Scroll & Zoom</code></td><td>Toggle based on preference</td></tr>
    <tr><td>Three-Finger Drag</td><td><code>Accessibility</code> → <code>Pointer Control</code></td><td>Enable Trackpad Options → Three Finger Drag</td></tr>
    <tr><td>Right Click</td><td><code>Trackpad</code> → <code>Point & Click</code></td><td>Secondary click → Click with Two Fingers</td></tr>
  </tbody>
</table>

#### 🖥️ Finder & Desktop
<table class="shortcuts-table">
  <thead>
    <tr><th>Setting</th><th>Path</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td>Show Extensions</td><td><code>Finder Settings</code> → <code>Advanced</code></td><td>Check Show all filename extensions</td></tr>
    <tr><td>Show Path Bar</td><td><code>Finder View Menu</code></td><td>Click Show Path Bar</td></tr>
    <tr><td>Show Status Bar</td><td><code>Finder View Menu</code></td><td>Click Show Status Bar</td></tr>
    <tr><td>New Window Location</td><td><code>Finder Settings</code> → <code>General</code></td><td>Set to Home Directory</td></tr>
    <tr><td>Search Scope</td><td><code>Finder Settings</code> → <code>Advanced</code></td><td>Set to Search the Current Folder</td></tr>
    <tr><td>Clean Up</td><td>Right-click Desktop</td><td>Click Use Stacks</td></tr>
    <tr><td>Sidebar</td><td><code>Finder Settings</code> → <code>Sidebar</code></td><td>Check Movies, Music, Pictures, Home</td></tr>
  </tbody>
</table>

#### ⚓ Dock & Menu Bar
<table class="shortcuts-table">
  <thead>
    <tr><th>Setting</th><th>Path</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td>Auto-Hide Dock</td><td><code>Desktop & Dock</code></td><td>Turn on Automatically hide/show Dock</td></tr>
    <tr><td>Dock Size</td><td><code>Desktop & Dock</code></td><td>Adjust Size slider (Smaller)</td></tr>
    <tr><td>Magnification</td><td><code>Desktop & Dock</code></td><td>Turn on Magnification</td></tr>
    <tr><td>Battery %</td><td><code>Control Center</code> → <code>Battery</code></td><td>Turn on Show Percentage</td></tr>
    <tr><td>Sound Icon</td><td><code>Control Center</code> → <code>Sound</code></td><td>Always Show in Menu Bar</td></tr>
    <tr><td>Bluetooth Icon</td><td><code>Control Center</code> → <code>Bluetooth</code></td><td>Always Show in Menu Bar</td></tr>
  </tbody>
</table>

#### 🛡️ Security & Privacy
<table class="shortcuts-table">
  <thead>
    <tr><th>Setting</th><th>Path</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td>FileVault</td><td><code>Privacy & Security</code></td><td>Turn On (Disk Encryption) ⚠️</td></tr>
    <tr><td>Firewall</td><td><code>Network</code> → <code>Firewall</code></td><td>Turn On</td></tr>
    <tr><td>Hot Corners</td><td><code>Desktop & Dock</code></td><td>Set corner to Lock Screen</td></tr>
    <tr><td>Lock Screen</td><td><code>Lock Screen Settings</code></td><td>Require password Immediately</td></tr>
  </tbody>
</table>

#### ⚡ Performance & Power
<table class="shortcuts-table">
  <thead>
    <tr><th>Setting</th><th>Path</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td>Optimized Charge</td><td><code>Battery</code> → <code>Battery Health</code></td><td>Turn on Optimized Charging</td></tr>
    <tr><td>Night Shift</td><td><code>Displays</code></td><td>Schedule: Sunset to Sunrise</td></tr>
    <tr><td>Key Repeat</td><td><code>Keyboard</code></td><td>Rate: Fast, Delay: Short</td></tr>
  </tbody>
</table>

#### 🌐 Safari & Internet
<table class="shortcuts-table">
  <thead>
    <tr><th>Setting</th><th>Path</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td>Show Full URL</td><td><code>Safari Settings</code> → <code>Advanced</code></td><td>Check Show full website address</td></tr>
    <tr><td>Develop Menu</td><td><code>Safari Settings</code> → <code>Advanced</code></td><td>Check Show Develop menu</td></tr>
    <tr><td>Default Browser</td><td><code>Desktop & Dock</code></td><td>Select preference</td></tr>
  </tbody>
</table>

#### 🛠️ Miscellaneous
<table class="shortcuts-table">
  <thead>
    <tr><th>Setting</th><th>Path</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td>Siri</td><td><code>Siri & Spotlight</code></td><td>Disable if unused</td></tr>
    <tr><td>Updates</td><td><code>General</code> → <code>Software Update</code></td><td>Enable Security Responses</td></tr>
  </tbody>
</table>

[↑ Back to Top](#table-of-contents)

- --


### 🔗 Related Topics

- Keyboard Shortcuts (Comprehensive)
- Terminal Command Reference
- System Configuration

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

- --


### 🔗 Related Topics

- System Information & Hardware
- Audio Tools
- Productivity Apps

## Getting Started (Beginners)

### Apple Silicon (M-Series) Compatibility 🍎

* *M1/M2/M3/M4/M5 Macs Are Special!**

Your Mac has a special type of processor (chip) called "Apple Silicon".

| Feature | Intel Macs | Apple Silicon (M1-M5) |
|---------|------------|----------------------|
| **Architecture** | x86_64 | arm64 |
| **Apps** | All native | Native + Rosetta 2 |
| **Performance** | Standard | High Efficiency & Speed ⚡ |

* *Which Mac do you have?** 🟢
1. Click  (Apple menu) → "About This Mac"
2. Look at "Chip" or "Processor".

[↑ Back to Top](#table-of-contents)

- --


### 🔗 Related Topics

- System Information & Hardware
- Design Tools
- Virtualization

## System Information & Hardware

### Check Your Mac Specifications 🟢

* *Terminal Method:** 🟡

```bash

# Basic system information
sw_vers

# Detailed system info
system_profiler SPSoftwareDataType SPHardwareDataType

# Check if Apple Silicon or Intel
uname -m

# arm64 = Apple Silicon (M1-M5) | x86_64 = Intel
```

* *Installing Rosetta 2 (for Intel apps):** 🍎

```bash

# Install Rosetta 2 (one time only)
softwareupdate --install-rosetta
```

[↑ Back to Top](#table-of-contents)

- --


### 🔗 Related Topics

- Opening Terminal - Step by Step
- Getting Started (Beginners)
- Audio Tools

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

- --


### 🔗 Related Topics

- Getting Started (Beginners)

## Terminal Command Reference

### Beginner Terminal Commands 🟢

* *Navigation:**

```bash
pwd                 # Print Working Directory (Where am I?)
ls                  # List files
ls -la              # List all files (including hidden)
cd Documents        # Change Directory to Documents
cd ..               # Go back one folder
cd ~                # Go to Home folder
```

* *File Operations:**

```bash
touch file.txt      # Create empty file
mkdir NewFolder     # Create new folder
cp file.txt copy.txt # Copy file
mv file.txt NewLoc/ # Move file
rm file.txt         # Delete file (Careful!)
open .              # Open current folder in Finder
```

### Mid-Level Terminal Commands 🟡

* *System Management:**

```bash
top                 # Real-time process viewer
killall Safari      # Force close an app
uptime              # How long has Mac been on?
history             # Show command history
```

* *Network:**

```bash
ifconfig            # Network interfaces
ping google.com     # Check internet connection
curl ifconfig.me    # Get public IP
```

### Pro Terminal Commands 🟠

* *Advanced Operations:**

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

- --


### 🔗 Related Topics

- System Configuration
- Keyboard Shortcuts (Comprehensive)
- Beginner: Essentials

## System Configuration

### Finder Configuration 🟢

* *Show Hidden Files:** `Cmd + Shift + .`

* *Terminal Method:** 🟡
```bash

# Show hidden files
defaults write com.apple.finder AppleShowAllFiles -bool true
killall Finder

# Show path bar
defaults write com.apple.finder ShowPathbar -bool true
```

### Screenshot Configuration 🟡

* *Terminal Tweaks:**
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

- --


### 🔗 Related Topics

- Advanced Configuration (Pro)
- Terminal Command Reference
- Beginner: Essentials

## Window Management Apps

Even with recent macOS updates adding window tiling, dedicated apps provide faster, keyboard-centric control (similar to Windows snapping).

### 1. Rectangle (Free & Open Source) 🟢
The most popular free option.
- **Website:** [rectangleapp.com](https://rectangleapp.com/)
- **Install via Homebrew:** `brew install --cask rectangle`
- **Key Shortcuts:**
  - `Ctrl + Opt + Left/Right`: Snap to halves
  - `Ctrl + Opt + Enter`: Maximize
  - `Ctrl + Opt + U/I/J/K`: Snap to corners

### 2. Magnet (Paid) 🟢
Excellent alternative if you prefer the App Store.
- **Availability:** Mac App Store
- **Features:** Drag-to-snap, clean menu bar interface, reliable performance.

↑ Back to Top


### 🔗 Related Topics

- Menu Bar Apps
- Remote Access
- Productivity Apps

## Menu Bar Apps

Keep your menu bar organized and clean.

### 1. Hidden Bar (Free) 🟢
A lightweight utility to hide menu bar icons.
- **Install:** `brew install --cask hiddenbar`

### 2. Ice (Free) 🟢
A modern, open-source alternative to Bartender.
- **Install:** `brew install --cask jordanbaird-ice`

### 3. Bartender (Paid) 🟢
The most powerful option for total control over menu bar items.


### 🔗 Related Topics

- Remote Access
- Productivity Apps
- Window Management Apps

## Productivity Apps

Boost your workflow with these powerful launchers and tools.

### 1. Raycast (Free for Personal Use) 🟢
The modern, extendable launcher that's taking over the Mac world.
- **Install:** `brew install --cask raycast`
- **Features:** Clipboard history, window management, extensions store, quick scripts.
- **Pro Tip:** Replace Spotlight (⌘ + Space) with Raycast in its settings.

### 2. Alfred (Freemium) 🟡
The veteran productivity app.
- **Install:** `brew install --cask alfred`
- **Features:** Incredibly fast file search, custom workflows (Powerpack required), clipboard history.

↑ Back to Top


### 🔗 Related Topics

- Menu Bar Apps
- Remote Access
- File Management

## Terminal Themes

Make your terminal look amazing and helpful with status indicators.

### 1. Oh My Zsh 🟡
A framework for managing your Zsh configuration.
- **Install:**
  ```bash
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  ```

### 2. Powerlevel10k Theme 🟠
The fastest and most customizable theme for Zsh.
1. **Install Font:** Download and install a Nerd Font (e.g., MesloLGS NF) for icons to work.
2. **Install Theme:**
   ```bash
   git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
   ```
3. **Activate:** Set `ZSH_THEME="powerlevel10k/powerlevel10k"` in your `~/.zshrc` file.
4. **Configure:** Restart terminal and type `p10k configure`.

↑ Back to Top


### 🔗 Related Topics

- Developer Tools (Mid-Level)

## Backup Strategies

Don't lose your data. Implement the "3-2-1" rule: 3 copies, 2 media types, 1 off-site.

### 1. Time Machine (Local) 🟢
Apple's built-in "set it and forget it" solution.
- **Setup:** `System Settings` → `General` → `Time Machine`.
- **Requirement:** External Hard Drive or NAS.
- **Tip:** Check "Encrypt Backup" to secure your data if the drive is stolen.

### 2. Cloud Backup (Off-site) 🟡
Protect against fire, theft, or hardware failure.
- **iCloud Drive:** Syncs Desktop & Documents (Good for access, not a full history backup).
- **Backblaze / Arq:** Dedicated backup services that run in the background and upload everything.

↑ Back to Top

- --

## Keyboard Shortcuts (Comprehensive)

<div class="shortcuts-controls">
  <select id="shortcuts-filter">
    <option value="all">Show All Categories</option>
    <option value="basics">The "Must Know" Basics</option>
    <option value="text">Text Editing & Document Control</option>
    <option value="finder">Finder & File Management</option>
    <option value="screenshots">Screenshots & Recording</option>
    <option value="web">Web Browsing</option>
    <option value="system">System & Window Management</option>
  </select>
  <button id="print-shortcuts-btn">🖨️ Print Shortcuts</button>
</div>

### 🔑 The "Must Know" Basics
<table class="shortcuts-table">
  <thead>
    <tr><th>Shortcut</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td><code>⌘</code> + <code>Space</code></td><td>Spotlight Search (Launch apps, find files, do math)</td></tr>
    <tr><td><code>⌘</code> + <code>Q</code></td><td>Quit application (Completely closes it)</td></tr>
    <tr><td><code>⌘</code> + <code>W</code></td><td>Close current window/tab</td></tr>
    <tr><td><code>⌘</code> + <code>Tab</code></td><td>Switch between open apps</td></tr>
    <tr><td><code>⌘</code> + <code>`</code></td><td>Switch between windows of the same app</td></tr>
    <tr><td><code>⌘</code> + <code>Opt</code> + <code>Esc</code></td><td>Force Quit menu (Use when app freezes)</td></tr>
    <tr><td><code>⌘</code> + <code>,</code></td><td>Open Settings/Preferences for current app</td></tr>
    <tr><td><code>⌘</code> + <code>H</code></td><td>Hide current app</td></tr>
    <tr><td><code>⌘</code> + <code>M</code></td><td>Minimize window to Dock</td></tr>
  </tbody>
</table>

### 📝 Text Editing & Document Control
<table class="shortcuts-table">
  <thead>
    <tr><th>Shortcut</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td><code>⌘</code> + <code>C</code></td><td>Copy</td></tr>
    <tr><td><code>⌘</code> + <code>V</code></td><td>Paste</td></tr>
    <tr><td><code>⌘</code> + <code>X</code></td><td>Cut</td></tr>
    <tr><td><code>⌘</code> + <code>Z</code></td><td>Undo</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>Z</code></td><td>Redo</td></tr>
    <tr><td><code>⌘</code> + <code>A</code></td><td>Select All</td></tr>
    <tr><td><code>⌘</code> + <code>F</code></td><td>Find / Search in document</td></tr>
    <tr><td><code>Opt</code> + <code>←</code> / <code>→</code></td><td>Move cursor by word</td></tr>
    <tr><td><code>⌘</code> + <code>←</code> / <code>→</code></td><td>Move cursor to start/end of line</td></tr>
    <tr><td><code>⌘</code> + <code>↑</code> / <code>↓</code></td><td>Move cursor to top/bottom of document</td></tr>
    <tr><td><code>Shift</code> + <code>Arrows</code></td><td>Highlight/Select text</td></tr>
    <tr><td><code>Opt</code> + <code>Delete</code></td><td>Delete previous word</td></tr>
    <tr><td><code>⌘</code> + <code>Delete</code></td><td>Delete entire line (to left of cursor)</td></tr>
  </tbody>
</table>

### 📂 Finder & File Management
<table class="shortcuts-table">
  <thead>
    <tr><th>Shortcut</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td><code>⌘</code> + <code>N</code></td><td>New Finder Window</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>N</code></td><td>Create New Folder</td></tr>
    <tr><td><code>Return</code></td><td>Rename selected file</td></tr>
    <tr><td><code>Spacebar</code></td><td>Quick Look (Preview file without opening)</td></tr>
    <tr><td><code>⌘</code> + <code>Delete</code></td><td>Move to Trash</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>Delete</code></td><td>Empty Trash</td></tr>
    <tr><td><code>⌘</code> + <code>D</code></td><td>Duplicate file</td></tr>
    <tr><td><code>⌘</code> + <code>I</code></td><td>Get Info (Size, type, permissions)</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>.</code></td><td>Toggle Hidden Files</td></tr>
    <tr><td><code>⌘</code> + <code>Opt</code> + <code>C</code></td><td>Copy File Path</td></tr>
    <tr><td><code>⌘</code> + <code>1</code>/<code>2</code>/<code>3</code>/<code>4</code></td><td>View as Icon / List / Column / Gallery</td></tr>
  </tbody>
</table>

### 📸 Screenshots & Recording
<table class="shortcuts-table">
  <thead>
    <tr><th>Shortcut</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>3</code></td><td>Capture Entire Screen</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>4</code></td><td>Capture Selected Area (Drag crosshair)</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>4</code> + <code>Space</code></td><td>Capture Specific Window (Camera icon appears)</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>5</code></td><td>Open Screenshot/Recording Utility (Options menu)</td></tr>
    <tr><td><code>Ctrl</code> + (Any above)</td><td>Copy screenshot to Clipboard instead of saving to file</td></tr>
  </tbody>
</table>

### 🌐 Web Browsing (Safari/Chrome)
<table class="shortcuts-table">
  <thead>
    <tr><th>Shortcut</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td><code>⌘</code> + <code>T</code></td><td>New Tab</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>T</code></td><td>Reopen Last Closed Tab (Lifesaver!)</td></tr>
    <tr><td><code>⌘</code> + <code>L</code></td><td>Highlight URL/Address Bar</td></tr>
    <tr><td><code>⌘</code> + <code>R</code></td><td>Refresh Page</td></tr>
    <tr><td><code>⌘</code> + <code>+</code> / <code>-</code></td><td>Zoom In / Out</td></tr>
    <tr><td><code>⌘</code> + <code>0</code></td><td>Reset Zoom</td></tr>
    <tr><td><code>Ctrl</code> + <code>Tab</code></td><td>Next Tab</td></tr>
    <tr><td><code>Ctrl</code> + <code>Shift</code> + <code>Tab</code></td><td>Previous Tab</td></tr>
  </tbody>
</table>

### 🖥️ System & Window Management
<table class="shortcuts-table">
  <thead>
    <tr><th>Shortcut</th><th>Action</th></tr>
  </thead>
  <tbody>
    <tr><td><code>Ctrl</code> + <code>⌘</code> + <code>F</code></td><td>Toggle Full Screen</td></tr>
    <tr><td><code>Ctrl</code> + <code>↑</code></td><td>Mission Control (See all open windows)</td></tr>
    <tr><td><code>Ctrl</code> + <code>↓</code></td><td>App Expose (See windows of current app)</td></tr>
    <tr><td><code>Ctrl</code> + <code>←</code> / <code>→</code></td><td>Switch between Desktops/Spaces</td></tr>
    <tr><td><code>Fn</code> + <code>Delete</code></td><td>Forward Delete (Delete character to right)</td></tr>
    <tr><td><code>Ctrl</code> + <code>⌘</code> + <code>Q</code></td><td>Lock Screen immediately</td></tr>
    <tr><td><code>⌘</code> + <code>Shift</code> + <code>?</code></td><td>Open Help Menu (Search for menu items!)</td></tr>
  </tbody>
</table>

[↑ Back to Top](#table-of-contents)

- --


### 🔗 Related Topics

- Beginner: Essentials
- Terminal Command Reference
- Troubleshooting Guide

## Troubleshooting Guide

### Common Issues & Fixes 🟢

* *1. App is Frozen**
- Press `Cmd + Option + Esc` to open Force Quit menu.
- Select the app and click "Force Quit".
- *Terminal way:* `killall AppName`

* *2. Mac is Slow**
- Open **Activity Monitor** (Cmd + Space, type "Activity Monitor").
- Check "CPU" and "Memory" tabs to see what's using resources.
- Restart your Mac (clears RAM and caches).

* *3. WiFi Issues**
- Toggle WiFi off and on.
- *Terminal reset:* `sudo killall -HUP mDNSResponder` (Flushes DNS).

* *4. Disk Full?**
- Check storage:  → System Settings → General → Storage.
- Use `du -sh *` in Terminal to find large folders.

### Safe Mode 🟡
- **Apple Silicon:** Shut down. Press and hold Power button until "Loading startup options" appears. Select disk, hold Shift, click "Continue in Safe Mode".
- **Intel:** Restart and immediately hold Shift.

[↑ Back to Top](#table-of-contents)

- --


### 🔗 Related Topics

- Keyboard Shortcuts (Comprehensive)
- Beginner: Essentials

## Developer Tools (Mid-Level)

### 1. Xcode Command Line Tools 🟡
Essential for development on macOS.
```bash
xcode-select --install
```

### 2. Homebrew (The Missing Package Manager) 🟡
Install software easily from terminal.

* *Install Homebrew:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

* *Common Commands:**
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

### 5. Containerization (Docker / OrbStack) 🟡
Run containers and Linux machines on your Mac.

- **OrbStack:** Fast, light, and native. The modern choice for Apple Silicon.
  - `brew install --cask orbstack`
- **Docker Desktop:** The industry standard.
  - `brew install --cask docker`

[↑ Back to Top](#table-of-contents)

- --


### 🔗 Related Topics

- Virtualization
- Terminal Themes
- Gaming on Mac

## Homebrew Essentials

Must-have CLI tools to supercharge your terminal.

### 1. tldr (Too Long; Didn't Read) 🟢
Simplified man pages.
- **Install:** `brew install tldr`
- **Usage:** `tldr tar` (Shows practical examples instead of a wall of text).

### 2. htop / btop 🟡
Interactive process viewer. Better than `top`.
- **Install:** `brew install htop` or `brew install btop`

### 3. ffmpeg 🔴
The swiss-army knife of video/audio conversion.
- **Install:** `brew install ffmpeg`
- **Usage:** `ffmpeg -i input.mp4 output.mp3`

### 4. bat 🟢
A `cat` clone with syntax highlighting.
- **Install:** `brew install bat`

↑ Back to Top

- --

## Virtualization

Run Windows or Linux on your Mac.

### 1. UTM (Free / Open Source) 🟢
Best for running generic Linux distros or emulating older architectures (x86 on Apple Silicon).
- **Install:** `brew install --cask utm`
- **Pros:** Free, native Apple Virtualization Framework support.

### 2. VMware Fusion Pro (Free for Personal Use) 🟡
Industry standard virtualization, now free for personal use (Broadcom).
- **Pros:** Robust networking, good 3D acceleration, reliable.

### 3. Parallels Desktop (Paid) 🟢
The most polished experience for running Windows on Mac.
- **Pros:** Easiest setup, "Coherence" mode (run Windows apps like Mac apps), best gaming performance.

↑ Back to Top


### 🔗 Related Topics

- Getting Started (Beginners)
- Gaming on Mac
- Developer Tools (Mid-Level)

## Gaming on Mac

Gaming on Apple Silicon has improved significantly with translation layers.

### 1. Whisky (Free / Open Source) 🟢
A user-friendly graphical wrapper for Wine and Apple's Game Porting Toolkit.
- **Best for:** Running Windows games without a full Windows VM.
- **Install:** `brew install --cask whisky`
- **Features:** Easy setup, manages "bottles" (containers) for games.

### 2. Game Porting Toolkit (GPTK) 🔴
Apple's translation layer allowing DirectX 12 games to run on macOS.
- **Usage:** Usually accessed via Whisky or CrossOver, but can be used via Terminal for advanced users.
- **Performance:** Surprisingly good for many AAA titles.

↑ Back to Top


### 🔗 Related Topics

- Virtualization
- How to Use This Guide
- Developer Tools (Mid-Level)

## Creative Tools

Professional grade creative software that runs natively on Apple Silicon.

### 1. DaVinci Resolve (Free / Paid) 🟠
Hollywood-grade video editing and color correction.
- **Install:** `brew install --cask davinci-resolve` (or via App Store)
- **Performance:** Highly optimized for M-Series chips.

### 2. Blender (Free & Open Source) 🟠
3D creation suite (Modeling, Rigging, Animation, Rendering).
- **Install:** `brew install --cask blender`

### 3. OBS Studio (Free & Open Source) 🟡
Live streaming and screen recording.
- **Install:** `brew install --cask obs`

↑ Back to Top


### 🔗 Related Topics

- Music Production
- Audio Tools
- Utilities

## Design Tools

Create stunning user interfaces and graphics.

### 1. Figma (Free / Paid) 🟢
The industry standard for interface design and prototyping.
- **Platform:** Web-based but has a solid macOS app.
- **Best for:** UI/UX design, collaboration.

### 2. Sketch (Paid) 🟠
The original Mac-native design tool.
- **Best for:** Designers who prefer a strictly native Mac app experience.

### 3. Affinity Designer (Paid) 🟢
A powerful, one-time purchase alternative to Adobe Illustrator.
- **Best for:** Vector graphics, illustrations, icons.
- **Performance:** Incredible speed on Apple Silicon.

↑ Back to Top


### 🔗 Related Topics

- Getting Started (Beginners)
- Music Production
- Virtualization

## Audio Tools

Route and record audio between applications.

### 1. Loopback (Paid) 🟠
Cable-free audio routing. Combine audio from multiple sources (e.g., Mic + Music) into one virtual input.
- **Use Case:** Podcasting, streaming, screen recording with system audio.

### 2. Audio Hijack (Paid) 🟠
Record any audio on your Mac.
- **Features:** Record individual apps (Zoom, Safari) separate from system audio. Apply effects in real-time.

↑ Back to Top


### 🔗 Related Topics

- System Information & Hardware
- Opening Terminal - Step by Step
- Creative Tools

## Music Production

Create music with industry-standard tools.

### 1. Logic Pro (Paid) 🟠
Apple's professional Digital Audio Workstation (DAW).
- **Features:** Massive sound library, spatial audio tools, professional mixing plugins.
- **Performance:** Optimized perfectly for Apple Silicon.

### 2. GarageBand (Free) 🟢
The best entry-level music creation tool.
- **Included:** Comes pre-installed on your Mac.
- **Path:** Great starting point before upgrading to Logic Pro.

↑ Back to Top


### 🔗 Related Topics

- Design Tools
- Creative Tools
- Getting Started (Beginners)

## Quick Look Plugins

Enhance macOS Quick Look (Spacebar preview) to support more file types.

### 1. Syntax Highlight (Free) 🟢
Adds syntax highlighting to code files (.js, .py, .json, etc.) in Quick Look.
- **Install:** `brew install --cask syntax-highlight`

### 2. QLVideo (Free) 🟢
Generates thumbnails and previews for video formats macOS doesn't natively support (mkv, flv, etc.).
- **Install:** `brew install --cask qlvideo`

### 3. QLMarkdown (Free) 🟢
Preview Markdown files rendered as HTML.
- **Install:** `brew install --cask qlmarkdown`

↑ Back to Top

- --

## Advanced Configuration (Pro)

### Shell Customization (Zsh) 🟠
Your configuration file is at `~/.zshrc`.

* *Useful Aliases:**
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


### 🔗 Related Topics

- System Configuration
- Terminal Command Reference

## Privacy & Security Deep Dive

Take control of your data and network connections.

### 1. Outbound Firewalls 🟠
macOS has an inbound firewall, but these tools stop apps from "phoning home".

- **LuLu (Free & Open Source):** Lightweight firewall by Objective-See. Blocks unknown outgoing connections.
  - **Install:** `brew install --cask lulu`
- **Little Snitch (Paid):** The power-user standard. Visualizes traffic map, granular rules, and bandwidth monitoring.

### 2. Malware Monitoring 🟠
Tools to detect persistence (malware that starts when your Mac starts).

- **KnockKnock (Free):** Scans for persistently installed software.


### 🔗 Related Topics

- Networking Tools
- Utilities
- Menu Bar Apps

## Maintenance & Cleaning

Keep your Mac running smooth and recover disk space.

### 1. OnyX (Free) 🟠
The swiss-army knife of macOS maintenance.
- **Use for:** Rebuilding databases, cleaning deep system caches, verifying file structure.
- **Warning:** Read instructions carefully before running tasks.

### 2. DaisyDisk (Paid) 🟢
The most beautiful way to visualize what's taking up space.
- **Alternative (Free):** `GrandPerspective` or `OmniDiskSweeper`.

### 3. AppCleaner (Free) 🟢
Uninstall apps completely by finding all associated files (plists, caches) scattered across the system.

### 4. Disk Space Analyzer (Terminal) 🟠
Find what's eating your storage without installing GUI apps.

```bash

# List sizes of folders in current directory (Human readable)
du -sh * | sort -hr

# Find files larger than 500MB
find . -type f -size +500M

# Visual Analyzer (NCurses Disk Usage) - Highly Recommended!
brew install ncdu && ncdu
```


### 🔗 Related Topics

- Terminal Command Reference

## Networking Tools

Analyze traffic and monitor connections.

### 1. Wireshark (Free / Open Source) 🔴
The world's most widely-used network protocol analyzer.
- **Install:** `brew install --cask wireshark`
- **Use Case:** Deep packet inspection, troubleshooting network issues, development.

### 2. Little Snitch (Paid) 🟠
The ultimate network monitor and application firewall.
- **Features:** Real-time traffic map, per-app connection alerts, bandwidth usage history.
- **Why use it:** See exactly where your data is going.

### 3. Network Speed Test
<div id="speed-test-widget" class="glass-card">
  <div class="speed-controls">
    <div id="speed-result">0.00 Mbps</div>
    <button id="start-speed-test">Start Speed Test</button>
  </div>
  <div id="speed-status">Ready to test download speed</div>
</div>


### 🔗 Related Topics

- Privacy & Security Deep Dive
- Utilities

## Remote Access

Control your Mac remotely or access other machines.

### 1. SSH (Secure Shell) 🟠
Access your Mac's terminal from another device.
- **Enable:** `System Settings` → `General` → `Sharing` → Turn on **Remote Login**.
- **Connect:** `ssh username@ip-address`

### 2. Screen Sharing (VNC) 🟢
View and control your Mac's screen from another Apple device.
- **Enable:** `System Settings` → `General` → `Sharing` → Turn on **Screen Sharing**.
- **Connect:** Finder → Go → Connect to Server → `vnc://ip-address`

### 3. Microsoft Remote Desktop (Free) 🟡
The best way to access a Windows PC from your Mac.
- **Install:** Mac App Store or `brew install --cask microsoft-remote-desktop`


### 🔗 Related Topics

- Menu Bar Apps
- Productivity Apps
- Window Management Apps

## File Management

Go beyond Finder with dual-pane file managers for power users.

### 1. Commander One (Freemium) 🟡
Classic dual-pane file manager inspired by Norton Commander.
- **Install:** `brew install --cask commander-one`
- **Features:** Built-in terminal, root access, archive support.

### 2. ForkLift (Paid) 🟠
A robust dual-pane file manager and file transfer client.
- **Install:** `brew install --cask forklift`
- **Best for:** Connecting to remote servers (SFTP, S3) and local file management.


### 🔗 Related Topics

- Clipboard Managers
- Productivity Apps
- Remote Access

## System Monitoring

Keep an eye on your CPU, GPU, RAM, and sensors.

### 1. Stats (Free & Open Source) 🟢
The best free menu bar monitor for macOS.
- **Install:** `brew install --cask stats`
- **Features:** Clean, customizable graphs for every system metric.

### 2. iStat Menus (Paid) 🟢
The gold standard for system monitoring with beautiful weather and calendar integration.

### 3. Activity Monitor (Built-in) 🟢
- **Tip:** View → Dock Icon → Show CPU Usage (Turn your dock icon into a live graph).
- **Tip:** Check "Memory Pressure" (Green is good, Yellow/Red means you need more RAM).


### 🔗 Related Topics

- Finance & Budgeting
- Calendar & Task Apps
- Menu Bar Apps

## Browser Extensions

Essential tools for privacy and security.

### 1. uBlock Origin (Free / Open Source) 🟢
The most efficient content blocker.
- **Best for:** Chrome, Firefox, Brave.
- **Note:** For Safari, consider **AdGuard** or **Wipr** due to extension limitations.

### 2. 1Password (Paid) 🟢
Securely manage passwords and passkeys.
- **Integration:** Unlocks with Touch ID on your Mac.
- **Alternative (Free):** Bitwarden.


### 🔗 Related Topics

- Email Clients
- Database Tools

## Communication Apps

Stay connected with teams and communities.

### 1. Slack (Freemium) 🟢
- **Tip:** `Cmd + K` (Quick Switcher) to jump to any channel or DM instantly.
- **Tip:** `Cmd + Shift + Enter` to create a new snippet.

### 2. Discord (Free) 🟢
- **Tip:** `Cmd + K` also works here for quick navigation!
- **Tip:** Adjust "Noise Suppression" (Krisp) in Voice settings for crystal clear audio.

### 3. Zoom (Free / Paid) 🟢
- **Mute Toggle:** `Cmd + Shift + A` (Audio).
- **Video Toggle:** `Cmd + Shift + V` (Video).

## Email Clients

Manage your inbox efficiently.

### 1. Spark (Freemium) 🟢
Smart email client with intelligent sorting.
- **Features:** Smart Inbox, "Gatekeeper" (block unwanted senders), team collaboration.

### 2. Mimestream (Paid) 🟢
A native macOS client for Gmail.
- **Best for:** Gmail users who want a fast, native app instead of a web wrapper.
- **Performance:** Incredible speed and system integration.

### 3. Apple Mail (Built-in) 🟢
Reliable, secure, and integrated.
- **Pros:** Privacy protection, Hide My Email integration, extensions support.


### 🔗 Related Topics

- Database Tools
- Browser Extensions
- Design Tools

## Calendar & Task Apps

Master your schedule and to-do list.

### 1. Fantastical (Freemium) 🟢
The best calendar app for macOS, period.
- **Features:** Natural language parsing (e.g., type "Lunch with John tomorrow at 1pm"), beautiful widgets, weather integration.

### 2. Things 3 (Paid) 🟢
The most polished and "Apple-like" task manager.
- **Design:** Award-winning minimalist interface.
- **Philosophy:** Based on GTD (Getting Things Done).
- **Alternative (Free):** Apple Reminders (which has gotten very good recently).


### 🔗 Related Topics

- Getting Started (Beginners)
- System Monitoring
- Virtualization

## Finance & Budgeting

Take control of your personal finances.

### 1. YNAB (You Need A Budget) (Paid) 🟢
The gold standard for zero-based budgeting.
- **Philosophy:** Give every dollar a job.
- **Features:** Bank syncing, goal tracking, detailed reports.

### 2. Banktivity (Paid) 🟠
A comprehensive personal finance manager for macOS.
- **Best for:** Tracking investments, real estate, and multi-currency support.
- **Privacy:** Local-first data storage options.


### 🔗 Related Topics

- System Monitoring

## Database Tools

Manage your local and remote databases with ease.

### 1. TablePlus (Freemium) 🟡
A modern, native, and friendly GUI tool for relational databases.
- **Supports:** PostgreSQL, MySQL, SQLite, Redis, and more.
- **Features:** Multiple tabs, code review, safe mode.

### 2. DBngin (Free) 🟢
The easiest way to get started with a local database server.
- **Use:** Spin up a local PostgreSQL, MySQL, or Redis server in one click.
- **Integration:** Works perfectly with TablePlus.


### 🔗 Related Topics

- Local Development
- Email Clients
- Browser Extensions

## Local Development

Spin up local servers for web development.

### 1. Laravel Herd (Free / Pro) 🟢
The fastest way to get started with PHP and Laravel development on macOS.
- **Features:** Zero dependencies (no Homebrew/Docker required), incredibly fast, native macOS app.
- **Includes:** Nginx, DNSMasq, PHP, Node.js.

### 2. MAMP (Free / Pro) 🟡
The classic Mac, Apache, MySQL, PHP stack.
- **Use:** Good for legacy projects or if you need a GUI for managing Apache/MySQL.

### 3. XAMPP (Free) 🟡
Open source cross-platform web server solution.
- **Use:** Widely used, but can be heavier than Herd.


### 🔗 Related Topics

- Database Tools

## Markdown Editors

Write notes, documentation, and blogs in style.

### 1. Obsidian (Free) 🟢
A powerful knowledge base that works on top of a local folder of plain text Markdown files.
- **Best for:** Personal Knowledge Management (PKM), linking notes, graph view.
- **Extensibility:** Massive community plugin ecosystem.

### 2. Bear (Freemium) 🟢
Beautiful, native Apple ecosystem note-taking app.
- **Best for:** Quick notes, aesthetics, Apple device sync (iCloud).
- **Design:** Minimalist and polished.

### 3. Typora (Paid) 🟢
A seamless "what you see is what you get" (WYSIWYG) markdown editor.
- **Best for:** Distraction-free writing where the markdown syntax hides as you type.


### 🔗 Related Topics

- Writing Tools
- Productivity Apps

## Writing Tools

Distraction-free environments for long-form writing.

### 1. Scrivener (Paid) 🟠
The ultimate tool for novelists, researchers, and scriptwriters.
- **Features:** Corkboard view, outliner, compile to ebook/PDF.
- **Best for:** Organizing massive writing projects.

### 2. Ulysses (Paid) 🟢
A polished, distraction-free writing app for the Apple ecosystem.
- **Features:** Markdown-based, seamless iCloud sync, direct publishing to WordPress/Medium.


### 🔗 Related Topics

- Markdown Editors

## Education & Research

Tools for students, researchers, and lifelong learners.

### 1. Zotero (Free & Open Source) 🟢
The best tool to collect, organize, cite, and share research.
- **Features:** Browser extension saves citations instantly, integrates with Word/Google Docs.

### 2. Anki (Free & Open Source) 🟢
Powerful, intelligent flashcards.
- **Method:** Uses Spaced Repetition to help you remember things forever.
- **Best for:** Language learning, medical school, memorizing shortcuts.

## Mind Mapping

Visualize your ideas and brainstorm effectively.

### 1. MindNode (Freemium) 🟢
The most beautiful and native mind mapping experience on Mac.
- **Best for:** Brainstorming, outlining, and visual organization.
- **Sync:** Seamless iCloud sync with iPhone/iPad.

### 2. XMind (Freemium) 🟡
A professional, cross-platform mind mapping tool.
- **Features:** Pitch mode, various chart structures (fishbone, matrix), and extensive export options.

## Utilities

Small but mighty tools that solve specific problems.

### 1. Amphetamine (Free) 🟢
Keep your Mac awake with powerful triggers.
- **Use:** Prevent sleep when a specific app is running or when connected to a specific WiFi.
- **Install:** Mac App Store.

### 2. The Unarchiver (Free) 🟢
Open any archive format (RAR, 7z, Tar, etc.) that macOS doesn't support natively.
- **Install:** `brew install --cask the-unarchiver`

### 3. CheatSheet (Free) 🟢
Hold the `⌘ Command` key to see a list of all active shortcuts for the current app.
- **Install:** `brew install --cask cheatsheet`


### 🔗 Related Topics

- Privacy & Security Deep Dive
- Menu Bar Apps
- Productivity Apps

## Clipboard Managers

Never lose a copied item again.

### 1. Maccy (Free / Open Source) 🟢
Lightweight, keyboard-centric clipboard manager.
- **Install:** `brew install --cask maccy`
- **Usage:** `Cmd + Shift + C` (default) to open history. Search and paste instantly.

### 2. Paste (Paid) 🟢
Visual clipboard history for Mac, iPhone, and iPad.
- **Features:** Sync across devices, pin items, visual preview of links/images.


### 🔗 Related Topics

- File Management
- Automation
- Productivity Apps

## Automation

Streamline repetitive tasks.

### 1. Shortcuts (Built-in) 🟢
Apple's modern automation tool.
- **Use:** Create cross-device workflows (Mac, iPhone, iPad).
- **Example:** "Split Screen" shortcut or "Batch Resize Images".

### 2. Automator (Built-in) 🟡
Legacy tool, great for file system operations.
- **Folder Actions:** Automatically process files dropped into a folder.
- **Quick Actions:** Add custom buttons to the Finder Touch Bar or Right-Click menu.


### 🔗 Related Topics

- Clipboard Managers
- Productivity Apps
- File Management

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

- --


### 🔗 Related Topics

- Terminal Command Reference

## 👥 Contributors

Thanks to these wonderful people: **kamalsoft**.

## Best Resources by Level

| Level | Resource | Description |
|-------|----------|-------------|
| 🟢 | [Apple Support](https://support.apple.com/mac) | Official guides |
| 🟡 | [MacRumors Guides](https://www.macrumors.com/guides/) | News and how-tos |
| 🟠 | [Homebrew Docs](https://docs.brew.sh/) | Package manager docs |
| 🔴 | [SS64 macOS Commands](https://ss64.com/osx/) | Complete command reference |
| 🔴 | [Hacker News](https://news.ycombinator.com/) | Tech news & discussion |
