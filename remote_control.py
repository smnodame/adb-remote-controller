#!/usr/bin/env python3
"""
ADB Remote Control Application
A desktop app to control Android devices via ADB commands
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading


class ADBRemoteControl:
    def __init__(self, root):
        self.root = root
        self.root.title("ADB Remote Control")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        self.selected_device = tk.StringVar()
        self.devices = []
        
        self.setup_ui()
        self.refresh_devices()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Device selection frame
        device_frame = ttk.LabelFrame(self.root, text="Device Selection", padding=10)
        device_frame.pack(fill="x", padx=10, pady=10)
        
        # Device dropdown
        ttk.Label(device_frame, text="Device:").grid(row=0, column=0, sticky="w", padx=5)
        self.device_combo = ttk.Combobox(
            device_frame, 
            textvariable=self.selected_device,
            state="readonly",
            width=30
        )
        self.device_combo.grid(row=0, column=1, padx=5, pady=5)
        
        # Refresh button
        ttk.Button(
            device_frame, 
            text="Refresh", 
            command=self.refresh_devices
        ).grid(row=0, column=2, padx=5)
        
        # Remote control frame
        remote_frame = ttk.LabelFrame(self.root, text="Remote Control", padding=20)
        remote_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Button style configuration
        button_config = {
            "width": 8,
            "height": 2,
            "font": ("Arial", 12, "bold")
        }
        
        # Navigation buttons layout (cross pattern)
        # Up button
        btn_up = tk.Button(
            remote_frame, 
            text="▲\nUP", 
            command=lambda: self.send_key("KEYCODE_DPAD_UP"),
            **button_config
        )
        btn_up.grid(row=0, column=1, padx=5, pady=5)
        
        # Left button
        btn_left = tk.Button(
            remote_frame, 
            text="◄\nLEFT", 
            command=lambda: self.send_key("KEYCODE_DPAD_LEFT"),
            **button_config
        )
        btn_left.grid(row=1, column=0, padx=5, pady=5)
        
        # OK/Center button
        btn_ok = tk.Button(
            remote_frame, 
            text="OK", 
            command=lambda: self.send_key("KEYCODE_DPAD_CENTER"),
            bg="#4CAF50",
            fg="white",
            **button_config
        )
        btn_ok.grid(row=1, column=1, padx=5, pady=5)
        
        # Right button
        btn_right = tk.Button(
            remote_frame, 
            text="►\nRIGHT", 
            command=lambda: self.send_key("KEYCODE_DPAD_RIGHT"),
            **button_config
        )
        btn_right.grid(row=1, column=2, padx=5, pady=5)
        
        # Down button
        btn_down = tk.Button(
            remote_frame, 
            text="▼\nDOWN", 
            command=lambda: self.send_key("KEYCODE_DPAD_DOWN"),
            **button_config
        )
        btn_down.grid(row=2, column=1, padx=5, pady=5)
        
        # Additional control buttons
        controls_frame = tk.Frame(remote_frame)
        controls_frame.grid(row=3, column=0, columnspan=3, pady=20)
        
        # Back button
        btn_back = tk.Button(
            controls_frame, 
            text="BACK", 
            command=lambda: self.send_key("KEYCODE_BACK"),
            bg="#FF9800",
            fg="white",
            **button_config
        )
        btn_back.grid(row=0, column=0, padx=10, pady=5)
        
        # Menu button
        btn_menu = tk.Button(
            controls_frame, 
            text="MENU", 
            command=lambda: self.send_key("KEYCODE_MENU"),
            bg="#2196F3",
            fg="white",
            **button_config
        )
        btn_menu.grid(row=0, column=1, padx=10, pady=5)
        
        # Home button (bonus)
        btn_home = tk.Button(
            controls_frame, 
            text="HOME", 
            command=lambda: self.send_key("KEYCODE_HOME"),
            bg="#9C27B0",
            fg="white",
            **button_config
        )
        btn_home.grid(row=1, column=0, padx=10, pady=5)
        
        # Power button (bonus)
        btn_power = tk.Button(
            controls_frame, 
            text="POWER", 
            command=lambda: self.send_key("KEYCODE_POWER"),
            bg="#F44336",
            fg="white",
            **button_config
        )
        btn_power.grid(row=1, column=1, padx=10, pady=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def get_adb_devices(self):
        """Query ADB for connected devices"""
        try:
            result = subprocess.run(
                ["adb", "devices"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                return []
            
            # Parse device list
            devices = []
            lines = result.stdout.strip().split("\n")
            for line in lines[1:]:  # Skip first line "List of devices attached"
                if line.strip() and "\tdevice" in line:
                    device_id = line.split("\t")[0]
                    devices.append(device_id)
            
            return devices
            
        except FileNotFoundError:
            messagebox.showerror(
                "ADB Not Found",
                "ADB is not installed or not in PATH.\n"
                "Please install Android Debug Bridge (ADB)."
            )
            return []
        except Exception as e:
            messagebox.showerror("Error", f"Error getting devices: {str(e)}")
            return []
    
    def refresh_devices(self):
        """Refresh the list of connected devices"""
        self.status_var.set("Refreshing devices...")
        self.root.update()
        
        self.devices = self.get_adb_devices()
        
        if not self.devices:
            self.device_combo["values"] = ["No devices found"]
            self.device_combo.current(0)
            self.status_var.set("No devices connected")
            messagebox.showwarning(
                "No Devices",
                "No ADB devices found.\n"
                "Please connect a device and enable USB debugging."
            )
        elif len(self.devices) == 1:
            # Auto-select if only one device
            self.device_combo["values"] = self.devices
            self.device_combo.current(0)
            self.status_var.set(f"Auto-selected: {self.devices[0]}")
        else:
            # Multiple devices found
            self.device_combo["values"] = self.devices
            self.device_combo.current(0)
            self.status_var.set(f"Found {len(self.devices)} devices")
    
    def send_key(self, keycode):
        """Send keycode to selected device"""
        device = self.selected_device.get()
        
        if not device or device == "No devices found":
            messagebox.showwarning(
                "No Device Selected",
                "Please select a device first."
            )
            return
        
        # Run in separate thread to avoid blocking UI
        thread = threading.Thread(
            target=self._send_key_thread,
            args=(device, keycode)
        )
        thread.daemon = True
        thread.start()
    
    def _send_key_thread(self, device, keycode):
        """Thread function to send ADB command"""
        try:
            self.status_var.set(f"Sending {keycode}...")
            
            result = subprocess.run(
                ["adb", "-s", device, "shell", "input", "keyevent", keycode],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                self.status_var.set(f"Sent {keycode}")
            else:
                self.status_var.set(f"Error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            self.status_var.set("Timeout: Command took too long")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = ADBRemoteControl(root)
    root.mainloop()


if __name__ == "__main__":
    main()
