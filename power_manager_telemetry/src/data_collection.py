import time
import random

def collect_data(knobs, duration):
    """
    Collect telemetry data over a specified duration.

    Parameters:
    - knobs: Configuration knobs for data collection
    - duration: Duration for which to collect data (in seconds)

    Returns:
    - List of telemetry data collected
    """
    end_time = time.time() + duration
    telemetry_data = []

    while time.time() < end_time:
        # Simulate data collection
        telemetry_data.append({
            "cpu_power": random.uniform(40, 100),  # Simulated CPU power
            "memory_power": random.uniform(20, 50),  # Simulated Memory power
            "nic_power": random.uniform(5, 15),  # Simulated NIC power
            "tdp_power": random.uniform(10, 25)  # Simulated TDP power
        })
        time.sleep(1)  # Sleep for 1 second before the next collection

    return telemetry_data
