import os
import subprocess

def run_traffic():
    # Simulate traffic to achieve 100% system utilization using stress-ng
    os.system("brew install stress-ng")  # Ensure stress-ng is installed
    subprocess.run(["stress-ng", "--cpu", "4", "--timeout", "60"])  # Run CPU stress test for 60 seconds
