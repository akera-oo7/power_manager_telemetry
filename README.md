# Power Manager Telemetry

## Description
In the era of 5G and edge computing, the deployment of devices across different locations has increased, leading to higher power consumption. To address this issue, the government is pushing enterprises and industries to reduce power usage. The goal is to achieve net-zero power consumption.

This project aims to measure and optimize power consumption in systems by:
1. Researching and identifying open-source tools for power measurement.
2. Identifying and documenting the available knobs in a system to measure power.
3. Collecting power telemetry data from CPU, memory, NIC, and TDP.
4. Measuring and recording system power utilization for CPU, NIC, and TDP based on the input parameter of system utilization percentage.
5. Creating a report on the power problem, technical approach, and results.

## Project Structure
- `data/`: Directory to store collected telemetry data.
- `src/`: Directory containing source code.
- `notebooks/`: Directory containing Jupyter notebooks for data analysis.
- `main.py`: Main script to run the project.
- `requirements.txt`: Python dependencies.

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Run the main script: `python main.py`
