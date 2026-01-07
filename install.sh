#!/bin/bash
# Installation script for ADB Remote Control
# This will install the 'adbremote' command to your system

set -e  # Exit on error

echo "Installing ADB Remote Control..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/remote_control.py"

# Make the Python script executable
echo "Making remote_control.py executable..."
chmod +x "$PYTHON_SCRIPT"

# Create symlink in /usr/local/bin
echo "Creating 'adbremote' command..."
sudo ln -sf "$PYTHON_SCRIPT" /usr/local/bin/adbremote

echo ""
echo "✓ Installation complete!"
echo ""
echo "You can now run 'adbremote' from anywhere in your terminal."
echo ""
echo "To uninstall, run: sudo rm /usr/local/bin/adbremote"
