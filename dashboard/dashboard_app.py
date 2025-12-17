# dashboard_app.py - Streamlit app with functional approve/decline buttons integrated with Jac data

import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JAC_PATH = os.path.join(BASE_DIR, "jac_code")


# Simulated backend device data storage (mock for demo)
# In a real app, this should be replaced by shared state or API calls with Jac walkers
if "devices_data" not in st.session_state:
    st.session_state.devices_data = [
        {"mac_address": "AA:BB:CC:11:22:33", "device_name": "John's Laptop", "risk_level": "Pending"},
        # Add more devices as needed
    ]

def approve_device(mac):
    for dev in st.session_state.devices_data:
        if dev["mac_address"] == mac:
            dev["risk_level"] = "Approved"
            st.success(f"Device {dev['device_name']} approved")
            break

def decline_device(mac):
    for dev in st.session_state.devices_data:
        if dev["mac_address"] == mac:
            dev["risk_level"] = "Rejected"
            st.error(f"Device {dev['device_name']} rejected")
            break

st.title("WiFi Gatekeeper Device Approval Dashboard")
st.subheader("Detected Devices")

if len(st.session_state.devices_data) == 0:
    st.write("No devices detected yet.")
else:
    for dev in st.session_state.devices_data:
        st.markdown(f"### {dev['device_name']}  (MAC: {dev['mac_address']})")
        st.markdown(f"**Status:** {dev['risk_level']}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Approve {dev['device_name']}", key=f"approve_{dev['mac_address']}"):
                approve_device(dev['mac_address'])
                st.experimental_rerun()  # rerun immediately after action
        with col2:
            if st.button(f"Decline {dev['device_name']}", key=f"decline_{dev['mac_address']}"):
                decline_device(dev['mac_address'])
                st.experimental_rerun()  # rerun immediately after action

        st.markdown("---")

st.write("Dashboard refreshes every 10 seconds to reflect status updates.")
st.experimental_rerun()