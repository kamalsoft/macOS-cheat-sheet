# macOS Complete Cheat Sheet
### From Beginner to Expert | M1/M2/M3/M4/M5 Compatible

![macOS Logo](https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png)

---

## 📋 Table of Contents

* [How to Use This Guide](#how-to-use-this-guide)
* [Opening Terminal - Step by Step](#opening-terminal---step-by-step)
* [Getting Started (Beginners)](#getting-started-beginners)
* [System Information & Hardware](#system-information--hardware)
* [Terminal Command Reference](#terminal-command-reference)
* [System Configuration](#system-configuration)
* [Keyboard Shortcuts](#keyboard-shortcuts)
* [Troubleshooting Guide](#troubleshooting-guide)
* [Developer Tools (Mid-Level)](#developer-tools-mid-level)
* [Advanced Configuration (Pro)](#advanced-configuration-pro)
* [Expert-Level Techniques](#expert-level-techniques)
* [Best Resources by Level](#best-resources-by-level)
* [Getting Help](#getting-help)

---

## How to Use This Guide

This cheat sheet is organized by skill level. Find your level and start there:

| Level | Description | Start Here |
|-------|-------------|-----------|
| 🟢 **Beginner** | New to Mac, learning basics | [Getting Started](#getting-started-beginners) |
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

---

## Opening Terminal - Step by Step

### Method 1: Using Spotlight Search (Easiest) 🟢

1. **Press** `Command (⌘) + Space` on your keyboard
   - The Command key is next to the space bar
   - A search box will appear in the center of your screen

2. **Type** `terminal` (you'll see it appear as you type)

3. **Press** `Return (Enter)` or click on "Terminal.app"

4. **Terminal window opens!** 
   - You'll see a white or black window with text
   - The cursor blinks, waiting for your commands

### Method 2: Using Finder 🟢

1. **Click** on the Finder icon (the smiling face) in your Dock
   - The Dock is the bar at the bottom of your screen

2. **Click** on "Applications" in the left sidebar
   - If you don't see it, click "Go" in the menu bar → Applications

3. **Open** the "Utilities" folder
   - Scroll down to find it, or press "U" to jump to it

4. **Double-click** on "Terminal"
   - The Terminal app has a black square icon

### Method 3: Using Launchpad 🟢

1. **Open** Launchpad
   - Press `F4` key, OR
   - Click the Launchpad icon in your Dock (looks like a rocket), OR
   - Pinch together with thumb and three fingers on trackpad

2. **Type** `terminal` in the search box that appears

3. **Click** on the Terminal icon

### First Time Using Terminal? 🟢

When Terminal opens, you'll see something like:
```
Last login: Sun Jan 05 10:30:45 on ttys000
YourName@YourMac ~ %
```

**What this means:**
- `YourName` = Your Mac username
- `YourMac` = Your computer name
- `~` = You're in your Home folder
- `%` = Terminal is ready for your command

**Try your first command:**
1. Type: `echo "Hello, I'm using Terminal!"`
2. Press `Return (Enter)`
3. You'll see your message printed back!

💡 **Pro Tip:** Keep Terminal in your Dock for easy access:
- Right-click the Terminal icon in the Dock
- Select "Options" → "Keep in Dock"

---

## Getting Started (Beginners)

### What You'll Need 🟢

| Item | Why You Need It | Where to Get It |
|------|-----------------|-----------------|
| **Mac Computer** | Any Mac with macOS | You have this! |
| **Power Adapter** | Keep your Mac charged | Came with your Mac |
| **Internet Connection** | Updates and downloads | WiFi or Ethernet |
| **Apple ID** | App Store, iCloud | Create at appleid.apple.com |
| **External Drive** | Backups (optional but recommended) | Any USB drive 256GB+ |

### Apple Silicon (M-Series) Compatibility 🍎

**M1/M2/M3/M4/M5 Macs Are Special!**

Your Mac has a special type of processor (chip) called "Apple Silicon" instead of Intel. Here's what you need to know:

| Feature | Intel Macs | Apple Silicon (M1-M5) |
|---------|------------|----------------------|
| **Speed** | Fast | Much Faster ⚡ |
| **Battery Life** | Good | Excellent 🔋 |
| **Apps** | All native | Some need Rosetta 2 |
| **Architecture** | x86_64 | arm64 |
| **Heat** | Can get warm | Runs cooler ❄️ |

**Which Mac do you have?** 🟢

1. Click the  (Apple menu) in top-left corner
2. Select "About This Mac"
3. Look at "Chip" or "Processor":
   - If it says **"Apple M1/M2/M3/M4/M5"** → You have Apple Silicon! 🍎
   - If it says **"Intel"** → You have an Intel Mac

**M5 Specific Features** (Latest generation) 🍎

- **M5**: Released in 2026, fastest chip yet
- **Enhanced AI/ML**: Better for creative apps
- **Memory**: Up to 128GB unified memory
- **Graphics**: Best for video editing and 3D work
- **Efficiency**: Even better battery life

### Complete First-Time Setup 🟢

#### Step 1: Turn On Your Mac

1. **Press the power button**
   - On laptops: Top-right corner of keyboard
   - On iMac: Back of computer, bottom-left
   - On Mac Studio/Mini: Back of device

2. **Wait for startup sound** (if enabled)
   - You'll see the Apple logo 

#### Step 2: Setup Assistant

The Setup Assistant will guide you through:

1. **Select Your Country/Region**
   - Click your country
   - Click "Continue"

2. **Choose Your Language**
   - Select preferred language
   - Click "Continue"

3. **Connect to WiFi**
   - Click your network name
   - Enter password
   - Click "Join"

4. **Data & Privacy**
   - Read the information
   - Click "Continue"

5. **Migration Assistant** (optional)
   - If you have another Mac: Choose "From a Mac, Time Machine backup, or startup disk"
   - If new to Mac: Choose "Not Now"

6. **Sign in with Apple ID**
   - Enter your Apple ID email
   - Enter password
   - Or click "Set Up Later" to skip

7. **Terms and Conditions**
   - Read (or not 😉)
   - Click "Agree"

8. **Create a Computer Account**
   - Enter your full name
   - Choose an account name (username)
   - Create a password
   - Add a hint (helps if you forget)

9. **Express Set Up**
   - For beginners: Click "Continue" (uses recommended settings)
   - For control: Click "Customize Settings"

10. **Enable Location Services**
    - Helps with Maps, weather, etc.
    - Recommended: Enable

11. **Analytics**
    - Choose whether to share usage data with Apple
    - Your choice!

12. **Screen Time** (optional)
    - Skip for now or set up

13. **Siri**
    - Enable if you want voice assistant
    - Say "Hey Siri" to test

14. **Choose Appearance**
    - Light, Dark, or Auto
    - You can change this anytime

15. **Welcome to Mac!** 🎉

#### Step 3: Essential First Settings 🟢

**System Settings** (Open by clicking  → System Settings)

1. **Apple ID Settings**
   - Click your name at top
   - Enable iCloud Drive
   - Enable Find My Mac (important!)

2. **Desktop & Dock**
   - Position: Bottom (recommended for beginners)
   - Size: Adjust slider to preference
   - Magnification: Try it out!

3. **Trackpad** (if using laptop)
   - Point & Click → Enable "Tap to click" (easier than pressing)
   - Scroll & Zoom → Natural scrolling (try both ways)
   - More Gestures → Enable all (very useful!)

4. **Displays**
   - Night Shift → Schedule: Sunset to Sunrise
   - True Tone → Enable (if available)

5. **Sound**
   - Test volume
   - Enable "Show Sound in menu bar"

6. **Touch ID & Password** (if available)
   - Add your fingerprint
   - Follows on-screen instructions

7. **Privacy & Security**
   - FileVault → Turn On (encrypts your disk) ⚠️
   - Allow apps from: App Store and identified developers

#### Step 4: Essential Apps Setup 🟢

**Safari (Web Browser)**
1. Open Safari from Dock
2. Set homepage: Safari menu → Preferences → General
3. Import bookmarks if needed

**Mail**
1. Open Mail app
2. Add your email account
3. Follow setup wizard

**Time Machine (Backups)** - DO THIS! Important! ⚠️
1. Connect external drive (USB)
2. System Settings → General → Time Machine
3. Click "+" to add backup disk
4. Turn on automatic backups

**App Store**
1. Open App Store from Dock
2. Sign in with Apple ID
3. Search and install apps you need

### Understanding Your Mac Desktop 🟢

```
┌─────────────────────────────────────────────┐
│  🍎 File Edit View ...            🔋 🔊 📅  │  ← Menu Bar
├─────────────────────────────────────────────┤
│                                             │
│          Your Desktop Space                 │
│                                             │
│     [Files and folders appear here]         │
│                                             │
│                                             │
└─────────────────────────────────────────────┘
    [📱💻📧🎵...]                                 ← Dock (apps)
```

**Key Areas:**
- **Menu Bar** (top): Time, battery, WiFi, etc.
- **Desktop**: Main work area
- **Dock** (bottom): Quick access to apps
- **Finder** (smiling face icon): File browser

### Basic Navigation 🟢

**Using the Finder** (Your file browser):

1. **Click** Finder icon (smiling face) in Dock

2. **Left Sidebar** shows:
   - **Favorites**: Quick access folders
   - **iCloud**: Cloud storage
   - **Locations**: Your Mac, external drives
   - **Tags**: Colored labels

3. **Main Window** shows:
   - Files and folders
   - Click once to select
   - Double-click to open

4. **Top Menu** changes based on what's open

**Creating Files and Folders:**

1. **New Folder**:
   - In Finder, press `⌘ + Shift + N`
   - Or: File menu → New Folder
   - Name it and press Return

2. **Moving Files**:
   - Click and drag to new location
   - Or: Cut (⌘+X), Navigate, Paste (⌘+V)

3. **Copying Files**:
   - Hold `Option` while dragging
   - Or: Copy (⌘+C), Navigate, Paste (⌘+V)

4. **Delete Files**:
   - Drag to Trash (in Dock)
   - Or: Select and press `⌘ + Delete`
   - Empty Trash: Right-click Trash → Empty Trash

---

## System Information & Hardware

### Check Your Mac Specifications 🟢

**Easy Method (GUI):**

1. Click  (Apple menu) → "About This Mac"
2. You'll see:
   - **Chip/Processor**: M1/M2/M3/M4/M5 or Intel
   - **Memory (RAM)**: Amount of RAM
   - **Startup Disk**: Storage space
   - **macOS Version**: Your OS version

**Detailed Information:**
- Click "More Info..." button
- Browse all system details

**Terminal Method:** 🟡

```bash
# Basic system information
sw_vers

# Output example:
# ProductName:    macOS
# ProductVersion: 14.2
# BuildVersion:   23C64

# Detailed system info
system_profiler SPSoftwareDataType SPHardwareDataType

# Check if Apple Silicon or Intel
uname -m
# arm64 = Apple Silicon (M1/M2/M3/M4/M5)
# x86_64 = Intel

# CPU information
sysctl -n machdep.cpu.brand_string

# Memory information
sysctl hw.memsize

# Check chip type
sysctl -n machdep.cpu.brand_string | grep -i "apple"
```

### M-Series Mac Specifics 🍎

**Check Your M-Series Generation:**

```bash
# Detailed chip information
system_profiler SPHardwareDataType | grep "Chip"

# Example outputs:
# Chip: Apple M1
# Chip: Apple M1 Pro
# Chip: Apple M1 Max
# Chip: Apple M1 Ultra
# Chip: Apple M2
# Chip: Apple M2 Pro
# Chip: Apple M2 Max
# Chip: Apple M2 Ultra
# Chip: Apple M3
# Chip: Apple M3 Pro
# Chip: Apple M3 Max
# Chip: Apple M4
# Chip: Apple M4 Pro
# Chip: Apple M4 Max
# Chip: Apple M5 (newest!)
```

**Installing Rosetta 2 (for Intel apps):** 🍎

Some older apps need Rosetta 2 to run on Apple Silicon:

```bash
# Install Rosetta 2 (one time only)
softwareupdate --install-rosetta
```

**Checking if App is Native or Rosetta:**

1. Open **Activity Monitor** (Applications → Utilities)
2. View → Columns → Kind
3. Look at the "Kind" column:
   - **Apple** = Native M-series app (best!)
   - **Intel** = Running through Rosetta 2

---

## Terminal Command Reference

### Beginner Terminal Commands 🟢

**Navigation (Moving Around):**

```bash
# See where you are
pwd
# Output: /Users/YourName (your current location)

# List files in current folder
ls
# Shows files and folders

# List with more details
ls -l
# Shows size, date, permissions

# List including hidden files (start with .)
ls -la

# Go to a folder
cd Documents
# Moves to Documents folder

# Go back one level
cd ..
# Moves up one folder

# Go to your home folder
cd ~
# ~ means home

# Go to specific path
cd /Applications
```

**File Operations (Working with Files):**

```bash
# Create a new empty file
touch myfile.txt

# Create a new folder
mkdir MyFolder

# Copy a file
cp file1.txt file2.txt
# Copies file1.txt to file2.txt

# Copy a folder and everything in it
cp -r Folder1 Folder2

# Move or rename a file
mv oldname.txt newname.txt
# Renames the file

# Move file to different folder
mv file.txt Documents/
# Moves file.txt into Documents folder

# Delete a file (careful! no undo)
rm file.txt

# Delete a folder and contents (very careful!)
rm -rf FolderName

# View file contents
cat file.txt
# Prints entire file

# View file page by page
less file.txt
# Press 'q' to quit
```

**Helpful Beginner Commands:**

```bash
# Clear the terminal screen
clear
# Or press: Control + L

# Get help for a command
man ls
# Shows manual for 'ls' command
# Press 'q' to exit

# See command history
history

# Repeat last command
!!

# Search for text in a file
grep "search word" file.txt

# Count lines in a file
wc -l file.txt

# Show first 10 lines of file
head file.txt

# Show last 10 lines of file
tail file.txt

# Show disk space usage
df -h

# Show folder size
du -sh FolderName

# Current date and time
date

# Who am I logged in as?
whoami

# Computer name
hostname
```

### Mid-Level Terminal Commands 🟡

**System Management:**

```bash
# System information
sw_vers                     # macOS version
system_profiler            # All system details
uname -a                   # Kernel information

# Check CPU temperature (needs additional tools)
sudo powermetrics --samplers smc | grep -i "CPU die temperature"

# Process monitoring
top                        # Real-time process viewer (press 'q' to quit)
ps aux                     # All running processes
ps aux | grep Safari       # Find Safari processes

# Kill a process
kill -9 PID_NUMBER         # Force kill by process ID
killall Safari             # Kill all Safari processes

# Check running services
launchctl list             # All services

# System uptime
uptime
```

**Package Management with Homebrew:** 🟡

```bash
# Install Homebrew (do this once)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Update Homebrew itself
brew update

# Upgrade all installed packages
brew upgrade

# Install a package
brew install wget
brew install git
brew install python3
brew install node

# Search for packages
brew search python

# List installed packages
brew list

# Uninstall a package
brew uninstall wget

# Get info about a package
brew info git

# Clean up old versions
brew cleanup

# Install GUI applications with Cask
brew install --cask visual-studio-code
brew install --cask google-chrome
brew install --cask slack
brew install --cask spotify
```

**Network Commands:**

```bash
# Show network interfaces
ifconfig

# Show WiFi interface only
ifconfig en0

# Get public IP address
curl ifconfig.me

# Get local IP address
ipconfig getifaddr en0

# Check internet connectivity
ping google.com
# Press Control+C to stop

# Trace network route
traceroute google.com

# DNS lookup
nslookup apple.com

# Show network connections
netstat -an

# WiFi information
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I

# Scan for WiFi networks
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s

# Flush DNS cache
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

**File Searching:**

```bash
# Find files by name
find ~ -name "*.txt"
# Finds all .txt files in home directory

# Find files modified in last 7 days
find ~ -mtime -7

# Find large files (over 100MB)
find ~ -size +100M

# Spotlight search from terminal
mdfind "search term"
mdfind -name "filename"

# Which command shows the path of a command
which python3
```

### Pro Terminal Commands 🟠

**Advanced File Operations:**

```bash
# Create symbolic link
ln -s /path/to/original /path/to/link

# Find and replace in files
sed -i '' 's/old/new/g' file.txt

# Archive and compress
tar -czf archive.tar.gz FolderName/

# Extract archive
tar -xzf archive.tar.gz

# Create zip file
zip -r archive.zip FolderName/

# Extract zip
unzip archive.zip

# Disk usage of folders
du -sh * | sort -hr

# Monitor file changes
fswatch /path/to/folder

# Sync folders
rsync -av source/ destination/
```

**System Administration:**

```bash
# View system logs
log show --predicate 'eventMessage contains "error"' --last 1h

# Check disk health
diskutil verifyVolume /

# List all disks
diskutil list

# Get disk info
diskutil info /dev/disk0

# Check file system
sudo fsck -fy

# View kernel extensions
kextstat

# System integrity check
sudo /usr/libexec/repair_packages --verify --standard-pkgs /

# Check system events
log stream

# Power management settings
pmset -g
pmset -g assertions
```

---

## System Configuration

### Finder Configuration 🟢

**Show Hidden Files** (files starting with .)

**Method 1 - Keyboard Shortcut** (Easiest!):
1. Open Finder
2. Press `Command + Shift + .` (period)
3. Hidden files appear grayed out
4. Press again to hide them

**Method 2 - Terminal** 🟡:
```bash
# Show hidden files
defaults write com.apple.finder AppleShowAllFiles -bool true
killall Finder

# Hide hidden files again
defaults write com.apple.finder AppleShowAllFiles -bool false
killall Finder
```

**Show File Extensions** 🟢

1. Open Finder
2. Finder menu → Settings (or Preferences)
3. Click "Advanced" tab
4. Check "Show all filename extensions"

**Show Path Bar** (shows current location) 🟢

1. Open Finder
2. View menu → Show Path Bar
3. You'll see the folder path at the bottom

**Show Status Bar** (shows file info) 🟢

1. Open Finder
2. View menu → Show Status Bar
3. Shows number of items and available space

**Terminal Method for All:** 🟡

```bash
# Show path bar
defaults write com.apple.finder ShowPathbar -bool true

# Show status bar
defaults write com.apple.finder ShowStatusBar -bool true

# Show full path in title
defaults write com.apple.finder _FXShowPosixPathInTitle -bool true

# Restart Finder
killall Finder
```

### Screenshot Configuration 🟡

**Change Screenshot Location:**

**GUI Method:** 🟢
1. Press `⌘ + Shift + 5`
2. Click "Options"
3. Choose save location
4. Close the tool

**Terminal Method:** 🟡
```bash
# Create Screenshots folder
mkdir ~/Desktop/Screenshots

# Change screenshot location
defaults write com.apple.screencapture location ~/Desktop/Screenshots

# Apply changes
killall SystemUIServer
```

**Change Screenshot Format:**

```bash
# Change to JPG (smaller files)
defaults write com.apple.screencapture type jpg

# Change to PNG (better quality - default)
defaults write com.apple.screencapture type png

# Other options: pdf, tiff, gif

# Apply changes
killall SystemUIServer
```

**Disable Screenshot Shadow:**

```bash
defaults write com.apple.screencapture disable-shadow -bool true
killall SystemUIServer

# Re-enable shadow
defaults write com.apple.screencapture disable-shadow -bool false
killall SystemUIServer
```

**Show Screenshot Thumbnail:**

```bash
# Disable floating thumbnail
defaults write com.apple.screencapture show-thumbnail -bool false
killall SystemUIServer

# Re-enable
defaults write com.apple.screencapture show-thumbnail -bool true
killall SystemUIServer
```

### Dock Configuration 🟡

**GUI Method:** 🟢

1.  → System Settings → Desktop & Dock
2. Adjust settings:
   - Size slider
   - Magnification
   - Position (Left, Bottom, Right)
   - Minimize windows using (Genie or Scale)
   - Automatically hide and show the Dock

**Terminal Method:** 🟡

```bash
# Auto-hide Dock
defaults write com.apple.dock autohide -bool true

# Don't auto-hide Dock
defaults write com.apple.dock autohide -bool false

# Change Dock position (left, bottom, right)
defaults write com.apple.dock orientation -string "left"

# Minimize windows into app icon
defaults write com.apple.dock minimize-to-application -bool true

# Speed up animation
defaults write com.apple.dock autohide-time-modifier -float 0.5

# Remove animation delay
defaults write com.apple.dock autohide-delay -float 0

# Make hidden apps transparent
defaults write com.apple.dock showhidden -bool true

# Show recent applications
defaults write com.apple.dock show-recents -bool true

# Apply all Dock changes
killall Dock
```

**Add Space Separator in Dock:** 🟡

```bash
# Add a space
defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="spacer-tile";}'
killall Dock

# Run multiple times for more spaces
```

### Menu Bar Configuration 🟡

```bash
# Hide Menu Bar automatically
defaults write NSGlobalDomain _HIHideMenuBar -bool true

# Show Menu Bar
defaults write NSGlobalDomain _HIHideMenuBar -bool false

# Flash date/time separators
defaults write com.apple.menuextra.clock FlashDateSeparators -bool true

# Show battery percentage
defaults write com.apple.menuextra.battery ShowPercent -string "YES"

# Restart SystemUIServer
killall SystemUIServer
```

### Performance Optimization 🟠

**Disable Animations:**

```bash
# Disable window animations
defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false

# Speed up Mission Control
defaults write com.apple.dock expose-animation-duration -float 0.1

# Faster Quick Look
defaults write NSGlobalDomain QLPanelAnimationDuration -float 0

# Remove Dock show delay
defaults write com.apple.dock autohide-delay -float 0

# Speed up dialog boxes
defaults write NSGlobalDomain NSWindowResizeTime -float 0.001

# Restart Dock
killall Dock
```

**Memory and Performance:**

```bash
# Clear RAM cache (careful!)
sudo purge

# Disable Spotlight indexing (not recommended)
sudo mdutil -a -i off

# Re-enable Spotlight
sudo mdutil -a -i on

# Rebuild Spotlight index
sudo mdutil -E /

# Check memory pressure
memory_pressure

# View detailed memory stats
vm_stat
```

---

## Keyboard Shortcuts

### Essential Shortcuts 🟢

**Every Mac User Must Know These!**

| Shortcut | Action | When to Use |
|----------|--------|-------------|
| **⌘ + Space** | Spotlight Search | Find anything instantly |
| **⌘ + Q** | Quit application | Close app completely |
| **⌘ + W** | Close window | Close current window |
| **⌘ + Tab** | Switch apps | Move between open apps |
| **⌘ + `** (backtick) | Switch windows | Same app, different windows |
| **⌘ + H** | Hide app | Hide current application |
| **⌘ + M** | Minimize | Minimize window to Dock |
| **⌘ + ,** | Preferences | Open app settings |
| **⌘ + S** | Save | Save your work |
| **⌘ + P** | Print | Print document |

💡 **Tip:** ⌘ is the Command key (next to spacebar)

### Text Editing Shortcuts 🟢

**Copy/Paste/Cut:**

| Shortcut | Action |
|----------|--------|
| **⌘ + C** | Copy |
| **⌘ + V** | Paste |
| **⌘ + X** | Cut |
| **⌘ + Z** | Undo |
| **⌘ + Shift + Z** | Redo |
| **⌘ + A** | Select All |
| **⌘ + F** | Find |
| **⌘ + G** | Find Next |

**Navigation:**

| Shortcut | Action |
|----------|--------|
| **⌘ + Left Arrow** | Beginning of line |
| **⌘ + Right Arrow** | End of line |
| **⌘ + Up Arrow** | Beginning of document |
| **⌘ + Down Arrow** | End of document |
| **Option + Left/Right** | Move by word |
| **⌘ + Backspace** | Delete line to left |

### Finder Shortcuts 🟢

| Shortcut | Action |
|----------|--------|
| **⌘ + N** | New Finder window |
| **⌘ + T** | New tab |
| **⌘ + Shift + N** | New folder |
| **⌘ + Delete** | Move to Trash |
| **⌘ + Shift + Delete** | Empty Trash |
| **⌘ + Shift + .** | Show/hide hidden files |
| **⌘ + I** | Get Info |
| **⌘ + D** | Duplicate |
| **⌘ + O** | Open |
| **Space** | Quick Look preview |
| **⌘ + 1/2/3/4** | View as Icons/List/Columns/Gallery |

### Screenshot Shortcuts 🟢

| Shortcut | What It Captures |
|----------|------------------|
| **⌘ + Shift + 3** | Entire screen |
| **⌘ + Shift + 4** | Selected area (drag to select) |
| **⌘ + Shift + 4 + Space** | Specific window (click window) |
| **⌘ + Shift + 5** | Screenshot tool (all options) |
| **⌘ + Shift + 6** | Touch Bar (if available) |

💡 **Add Control key to copy to clipboard instead of saving**

### Window Management 🟡

| Shortcut | Action |
|----------|--------|
| **⌃ + ⌘ + F** | Toggle full screen |
| **⌃ + Up** | Mission Control (all windows) |
| **⌃ + Down** | Application windows |
| **⌃ + Left/Right** | Switch between Spaces/Desktops |
| **F11** | Show Desktop |
| **⌃ + ⌘ + Q** | Lock screen |

**Symbols:**
- ⌘ = Command
- ⌃ = Control
- ⌥ = Option (Alt)
- ⇧ = Shift

### Force Quit Shortcuts 🟢

| Shortcut | Action |
|----------|--------|
| **⌘ + Option + Esc** | Force Quit
