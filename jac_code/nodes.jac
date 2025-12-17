node Device {
    has mac_address: str;
    has ip_address: str;
    has device_name: str;
    has risk_level: str = "unknown";
    has last_seen: float = 0.0;
}

node ConnectionEvent {
    has timestamp: float;
    has approved: bool = false;
    has denied: bool = false;
}

edge generated_event {}
edge event_device {}