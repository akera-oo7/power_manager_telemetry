from src import data_collection

def main():
    knobs = {}  # Define any necessary knobs for configuration
    duration = 10  # Duration for data collection in seconds

    # Collect telemetry data
    telemetry_data = data_collection.collect_data(knobs, duration)

    # Print collected telemetry data
    for index, data in enumerate(telemetry_data):
        print(f"Data point {index + 1}: {data}")

if __name__ == "__main__":
    main()
