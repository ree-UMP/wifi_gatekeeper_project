node DashboardUI {
    has device_list: list = [];
}

walker DashboardUpdater {
    can update_device_list with DashboardUI entry {
        device_list = [root --> Device];
        here.device_list = device_list;
        print(f"Dashboard updated with {len(device_list)} devices.");
    }
}