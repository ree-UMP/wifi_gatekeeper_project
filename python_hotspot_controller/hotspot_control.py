import time
import subprocess

def get_connected_devices():
    # Example command to get connected devices on a Linux system with hostapd
    try:
        result = subprocess.run(['iw', 'dev', 'wlan0', 'station', 'dump'], capture_output=True, text=True)
        stations = result.stdout.strip().split('\n\n')
        devices = []
        for station in stations:
            lines = station.split('\n')
            mac = lines[0].split()[1]
            devices.append(mac)
        return devices
    except Exception as e:
        print(f"Error getting connected devices: {e}")
        return []

def monitor_connections(poll_interval=5):
    known_devices = set()
    while True:
        current_devices = set(get_connected_devices())
        new_devices = current_devices - known_devices
        for mac in new_devices:
            print(f"New device detected: {mac}")
            # Here you would trigger Jac event or API call for new device detection
        known_devices = current_devices
        time.sleep(poll_interval)

if __name__ == "__main__":
    monitor_connections()