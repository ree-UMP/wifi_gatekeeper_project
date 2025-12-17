walker UserApproval {
    # Ability to approve a device, triggered by Device node at entry
    can approve with Device entry {
        here.risk_level = "Approved";
        print(f"Device {here.device_name} approved");
    }

    # Ability to reject a device, triggered by Device node at entry
    can reject with Device entry {
        here.risk_level = "Rejected";
        print(f"Device {here.device_name} rejected");
    }
}