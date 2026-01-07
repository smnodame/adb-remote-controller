#!/bin/bash
# Uninstallation script for ADB Remote Control

echo "Uninstalling ADB Remote Control..."

# Remove symlink from /usr/local/bin
if [ -L "/usr/local/bin/adbremote" ]; then
    echo "Removing 'adbremote' command..."
    sudo rm /usr/local/bin/adbremote
    echo "✓ Uninstallation complete!"
else
    echo "Command 'adbremote' not found in /usr/local/bin"
    echo "Nothing to uninstall."
fi
