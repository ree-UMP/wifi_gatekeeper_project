# jac_code/ui.jac
# Walkers for UI notifications and user responses

walker DeviceNotification {
    has device: Device;

    can send_notification with Device entry {
        print(f"Notification: Device {here.device_name} ({here.mac_address}) with risk {here.risk_level} detected.");
        # Integration to messaging or UI platforms can be added here
    }

    can user_response with Device entry {
        print(f"Waiting for user approval on device: {here.device_name} ({here.mac_address})");
        # Hook for UI interaction
    }
}