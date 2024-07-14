import pandas as pd
import matplotlib.pyplot as plt

def generate_report(power_data):
    # Generate and save a report
    plt.figure(figsize=(10, 6))
    plt.plot(power_data.index, power_data["total_power"], label="Total Power Consumption")
    plt.xlabel("Time")
    plt.ylabel("Power (W)")
    plt.title("System Power Consumption Over Time")
    plt.legend()
    plt.savefig("data/power_report.png")
