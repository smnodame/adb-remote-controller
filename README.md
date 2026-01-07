# ADB Remote Control

A desktop application for Ubuntu that provides a remote control interface for Android devices via ADB (Android Debug Bridge).

## Features

- 🎮 **Remote Control Interface**: Intuitive button layout mimicking a physical remote
- 📱 **Device Detection**: Automatically detects connected ADB devices
- 🔄 **Auto-Selection**: Automatically selects device if only one is connected
- 🎯 **Multiple Controls**: 
  - Navigation: Up, Down, Left, Right
  - OK/Enter button
  - Back button
  - Menu button
  - Bonus: Home and Power buttons

## Prerequisites

### System Requirements

- Ubuntu Linux (or other Linux distribution)
- Python 3.6 or higher
- Tkinter (Python GUI library)
- ADB (Android Debug Bridge)

### Installation

1. **Install Python and Tkinter**:
```bash
sudo apt update
sudo apt install python3 python3-tk
```

2. **Install ADB**:
```bash
sudo apt install android-tools-adb
```

3. **Verify ADB installation**:
```bash
adb --version
```

## Setup

1. **Enable USB Debugging on your Android device**:
   - Go to Settings → About Phone
   - Tap "Build Number" 7 times to enable Developer Options
   - Go to Settings → Developer Options
   - Enable "USB Debugging"

2. **Connect your device**:
   - Connect your Android device via USB cable
   - Accept the USB debugging authorization prompt on your device

3. **Verify device connection**:
```bash
adb devices
```

You should see your device listed.

## Running the Application

### Option 1: Install as System Command (Recommended)

Install the app so you can run it from anywhere using the `adbremote` command:

```bash
chmod +x install.sh
./install.sh
```

Then simply run:
```bash
adbremote
```

### Option 2: Run Directly

1. **Make the script executable** (optional):
```bash
chmod +x remote_control.py
```

2. **Run the application**:
```bash
python3 remote_control.py
```

Or if you made it executable:
```bash
./remote_control.py
```

## Usage

1. **Launch the app**: The application will automatically scan for connected ADB devices
2. **Device Selection**: 
   - If only one device is found, it will be automatically selected
   - If multiple devices are found, select one from the dropdown
   - Use the "Refresh" button to rescan for devices
3. **Control your device**: Click the buttons to send commands to your Android device

## Button Mappings

| Button | ADB Keycode | Function |
|--------|-------------|----------|
| UP | KEYCODE_DPAD_UP | Navigate up |
| DOWN | KEYCODE_DPAD_DOWN | Navigate down |
| LEFT | KEYCODE_DPAD_LEFT | Navigate left |
| RIGHT | KEYCODE_DPAD_RIGHT | Navigate right |
| OK | KEYCODE_DPAD_CENTER | Select/Enter |
| BACK | KEYCODE_BACK | Go back |
| MENU | KEYCODE_MENU | Open menu |
| HOME | KEYCODE_HOME | Go to home screen |
| POWER | KEYCODE_POWER | Power/Sleep button |

## Troubleshooting

### "ADB Not Found" Error
- Make sure ADB is installed: `sudo apt install android-tools-adb`
- Verify ADB is in PATH: `which adb`

### "No Devices Found"
- Check USB cable connection
- Ensure USB Debugging is enabled on your device
- Try running: `adb kill-server && adb start-server`
- Check device authorization

### Device Unauthorized
- Check your device screen for USB debugging authorization prompt
- Accept the prompt and optionally check "Always allow from this computer"

### Commands Not Working
- Verify device is properly connected: `adb devices`
- Try restarting ADB server: `adb kill-server && adb start-server`
- Check device screen is unlocked

## Wireless ADB (Optional)

You can also use this app with wireless ADB:

1. Connect device via USB first
2. Enable wireless debugging:
```bash
adb tcpip 5555
```
3. Find your device IP address (in device Settings → About Phone → Status)
4. Connect wirelessly:
```bash
adb connect <device_ip>:5555
```
5. Disconnect USB cable and use the app wirelessly!

## License

Free to use and modify as needed.

## Contributing

Feel free to enhance the application with additional features such as:
- Volume controls
- Text input
- Screenshot capture
- Screen recording controls
- Custom key sequences
# adb-remote-controller
