#!/bin/bash

# macOS Mastered - Setup Script
# Installs Homebrew and sets reasonable macOS defaults.

echo "----------------------------------------------------------------"
echo "  macOS Mastered Setup"
echo "----------------------------------------------------------------"
echo "⚠️  DISCLAIMER: This script modifies system settings."
echo "    Please review the code before running."
echo "    Press Ctrl+C to cancel or Enter to continue."
echo "----------------------------------------------------------------"
read -r

# 1. Install Homebrew
if ! command -v brew &> /dev/null; then
    echo "🍺 Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Add Homebrew to PATH for Apple Silicon
    if [[ $(uname -m) == 'arm64' ]]; then
        echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
        eval "$(/opt/homebrew/bin/brew shellenv)"
    fi
else
    echo "✅ Homebrew is already installed."
fi

# 2. System Configurations
echo "⚙️  Applying macOS defaults..."

# Close System Settings to prevent overriding
osascript -e 'tell application "System Settings" to quit'

# --- Finder ---
# Show all filename extensions
defaults write NSGlobalDomain AppleShowAllExtensions -bool true
# Show status bar
defaults write com.apple.finder ShowStatusBar -bool true
# Show path bar
defaults write com.apple.finder ShowPathbar -bool true
# Keep folders on top when sorting by name
defaults write com.apple.finder _FXSortFoldersFirst -bool true
# When performing a search, search the current folder by default
defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"
# Disable the warning when changing a file extension
defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false

# --- Dock ---
# Automatically hide and show the Dock
defaults write com.apple.dock autohide -bool true
# Don't show recent applications in Dock
defaults write com.apple.dock show-recents -bool false
# Minimize windows into their application’s icon
defaults write com.apple.dock minimize-to-application -bool true

# --- Screenshots ---
# Save screenshots to the Desktop/Screenshots folder
mkdir -p "${HOME}/Desktop/Screenshots"
defaults write com.apple.screencapture location -string "${HOME}/Desktop/Screenshots"
# Disable shadow in screenshots
defaults write com.apple.screencapture disable-shadow -bool true

# --- Trackpad ---
# Enable "Tap to click"
defaults write com.apple.AppleMultitouchTrackpad Clicking -bool true
defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad Clicking -bool true

# --- Keyboard ---
# Set a fast keyboard repeat rate
defaults write NSGlobalDomain KeyRepeat -int 2
defaults write NSGlobalDomain InitialKeyRepeat -int 15

# 3. Restart Services
echo "🔄 Restarting Finder and Dock..."
killall Finder
killall Dock
killall SystemUIServer

echo "----------------------------------------------------------------"
echo "✅ Setup Complete!"
echo "   Note: Some changes may require a logout/restart to take effect."
echo "----------------------------------------------------------------"