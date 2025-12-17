import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="WiFi Gatekeeper",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("📡 WiFi Gatekeeper")
st.caption("Admin dashboard for WiFi access control")

st.divider()

# ---------------- SESSION STATE INIT ----------------
if "wifi_name" not in st.session_state:
    st.session_state.wifi_name = None

if "pending_devices" not in st.session_state:
    st.session_state.pending_devices = []

if "connected_devices" not in st.session_state:
    st.session_state.connected_devices = []

# ---------------- WIFI REGISTRATION MODULE ----------------
st.subheader("📶 Register WiFi Network")

if not st.session_state.wifi_name:
    wifi_name = st.text_input("Enter WiFi name (SSID)")
    if st.button("Register WiFi"):
        if wifi_name:
            st.session_state.wifi_name = wifi_name
            st.success(f"WiFi '{wifi_name}' registered")
        else:
            st.warning("Please enter a WiFi name")
else:
    st.info(f"Managing network: **{st.session_state.wifi_name}**")

st.divider()

# ---------------- DEVICE DETECTION (DEMO SIMULATION) ----------------
def detect_device():
    return {
        "name": random.choice(["John’s Laptop", "Android Phone", "iPhone", "Tablet"]),
        "mac": f"AA:BB:{random.randint(10,99)}:{random.randint(10,99)}:{random.randint(10,99)}",
        "risk": random.choice(["Low", "Medium", "High"])
    }

if st.session_state.wifi_name:
    if st.button("🔍 Detect New Device"):
        st.session_state.pending_devices.append(detect_device())

# ---------------- PENDING DEVICES MODULE ----------------
st.subheader("🕒 Pending Devices")

if not st.session_state.pending_devices:
    st.write("No pending devices")
else:
    for i, device in enumerate(st.session_state.pending_devices):
        st.markdown(
            f"""
            **{device['name']}**  
            MAC: `{device['mac']}`  
            Risk: **{device['risk']}**
            """
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Approve", key=f"approve_{i}"):
                st.session_state.connected_devices.append(device)
                st.session_state.pending_devices.pop(i)
                st.rerun()

        with col2:
            if st.button("⛔ Decline", key=f"decline_{i}"):
                st.session_state.pending_devices.pop(i)
                st.rerun()

        st.divider()

# ---------------- CONNECTED DEVICES MODULE ----------------
st.subheader("🟢 Connected Devices")

if not st.session_state.connected_devices:
    st.write("No connected devices")
else:
    for i, device in enumerate(st.session_state.connected_devices):
        st.markdown(
            f"""
            **{device['name']}**  
            MAC: `{device['mac']}`  
            Risk: **{device['risk']}**
            """
        )

        if st.button("⛔ Disconnect", key=f"disconnect_{i}"):
            st.session_state.connected_devices.pop(i)
            st.rerun()

        st.divider()

# ---------------- FOOTER ----------------
st.caption("Demo mode • Real enforcement requires Linux hotspot integration")
