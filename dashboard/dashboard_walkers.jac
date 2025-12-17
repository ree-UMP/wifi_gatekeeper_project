walker DeviceListWalker {
    can list_devices with `root entry {
        devices = [root --> `?Device];
        for dev in devices {
            print(f"Device: {dev.device_name} ({dev.mac_address}) Risk: {dev.risk_level}");
        }
    }
}