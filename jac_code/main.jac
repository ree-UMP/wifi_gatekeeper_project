# jac_code/main.jac
# Main orchestration for WiFi Gatekeeper project

import from jac_code { DeviceMonitor, UserApproval, DeviceNotification }

with entry {
    # Simulate detecting a new device
    root spawn DeviceMonitor(mac_address="AA:BB:CC:11:22:33", device_name="John's Laptop", timestamp=1234567890.0);

    devices = [root --> (`?Device)];

    # Notify user and initiate approval for each detected device
    for dev in devices {
        root spawn DeviceNotification(device=dev);
        root spawn UserApproval(device=dev);
    }

    # Simulate user approving the first detected device
    if len(devices) > 0 {
        root spawn UserApproval(device=devices[0], decision="approve");
    }
}





