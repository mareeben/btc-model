import csv
import json
from datetime import datetime

# data source https://www.blockchain.com/explorer/charts/difficulty?timespan=all

if __name__ == "__main__":
    # Load data from JSON file
    with open("data_raw/blockchain_difficulty.json", "r") as file:
        data = json.load(file)
    

    # Function to convert UTC timestamp (milliseconds) to ISO 8601 format
    def convert_utc_to_datetime(utc_timestamp):
        return datetime.utcfromtimestamp(utc_timestamp / 1000).isoformat()


    # Prepare a dictionary to store combined data
    combined_data = {}

    # Process "difficulty" data
    for entry in data["difficulty"]:
        timestamp = convert_utc_to_datetime(entry["x"])
        if timestamp not in combined_data:
            combined_data[timestamp] = {}
        combined_data[timestamp]["difficulty"] = entry["y"]

    # Process "market-price" data
    for entry in data["market-price"]:
        timestamp = convert_utc_to_datetime(entry["x"])
        if timestamp not in combined_data:
            combined_data[timestamp] = {}
        combined_data[timestamp]["market-price"] = entry["y"]

    # Prepare the CSV output
    csv_file = "../notebooks/data/blockchain_difficulty.csv"

    # Open the CSV file for writing
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["Date", "difficulty", "market-price"])

        # Write the data rows
        for timestamp, metrics in sorted(combined_data.items()):
            writer.writerow([
                timestamp,
                metrics.get("difficulty", ""),  # Use an empty string if no value exists
                metrics.get("market-price", "")  # Use an empty string if no value exists
            ])

    print(f"Data has been successfully written to {csv_file}.")
