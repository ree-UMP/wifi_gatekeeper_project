test DeviceNodeTest {
    can create_device {
        dev = Device(mac_address="00:11:22:33:44:55", device_name="Test Device");
        assert dev.mac_address == "00:11:22:33:44:55";
        assert dev.device_name == "Test Device";
        assert dev.risk_level == "unknown";
    }
}