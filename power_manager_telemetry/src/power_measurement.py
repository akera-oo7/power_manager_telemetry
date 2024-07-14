import pandas as pd

def measure_power(telemetry_data):
    # Measure system power utilization
    # Example: Using simple metrics for demonstration
    power_data = telemetry_data.copy()
    power_data["total_power"] = telemetry_data["cpu"] * 0.5 + telemetry_data["memory"] * 0.3 + telemetry_data["nic"] * 0.2
    power_data.to_csv("data/power_data.csv", index=False)
    return power_data
