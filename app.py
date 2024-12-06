import streamlit as st
import psutil
import time
from datetime import datetime
from predict_model import predict  # Import the prediction function from the model script

# Streamlit App Layout
st.title("AI Model Prediction Dashboard")

# User Input: Define input fields for the required data
st.write("### Automatically Collected System Metrics")

# Function to collect system metrics
def collect_system_metrics():
    # Collect system metrics using psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # System load (1, 5, 15 minute averages)
    sys_load = psutil.getloadavg()

    # RAM usage
    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024 ** 3)  # Convert bytes to GB

    # Swap usage
    swap = psutil.swap_memory()
    swap_used = swap.used / (1024 ** 3)  # Convert bytes to GB

    # Root filesystem usage
    root_fs = psutil.disk_usage('/')
    root_fs_used = root_fs.used / (1024 ** 3)  # Convert bytes to GB

    return cpu_usage, sys_load, ram_used, swap_used, root_fs_used

# Function to get the current time
def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

# Collect metrics every 4 seconds
while True:
    # Collect system metrics
    cpu_usage, sys_load, ram_used, swap_used, root_fs_used = collect_system_metrics()

    # Get the current time
    current_time = get_current_time()

    # Display the current time

    # Display the collected system metrics with better formatting
    st.subheader("System Metrics")
    st.write(f" **Current Time:** {current_time}")

    st.write(f"**CPU Usage:** {cpu_usage}%")
    st.write(f"**System Load (1m, 5m, 15m):** {sys_load}")
    st.write(f"**RAM Used:** {ram_used:.2f} GB")
    st.write(f"**Swap Used:** {swap_used:.2f} GB")
    st.write(f"**Root Filesystem Used:** {root_fs_used:.2f} GB")

    # Gather system metrics into a dictionary to pass to the prediction function
    data = {
        'cpu_usage': [cpu_usage],
        'sys_load': [sys_load[0]],  # Using the 1-minute load average
        'ram_used': [ram_used],
        'swap_used': [swap_used],
        'root_fs_used': [root_fs_used]
    }

    # Call the prediction function with the collected system metrics
    prediction = predict(data)
    # Display the result
    if prediction[0] == 1:
        st.error(f"Il ya une anomalie")
    else:
        st.success(f"Pas d anomalie")

    # Wait for 4 seconds before rerunning the app
    time.sleep(4)

    # Stop current execution and trigger a rerun
