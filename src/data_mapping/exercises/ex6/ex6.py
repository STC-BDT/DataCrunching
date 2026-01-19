import requests
import csv
from collections import defaultdict

# API endpoint configuration
BASE_URL = "https://mobility.api.opendatahub.com/v2/flat%2Cnode/EnvironmentStation/*/2025-01-01/2025-01-05"
STATION_CODE = "BZ4"
LIMIT = 10


def fetch_page(offset: int, limit: int = LIMIT) -> dict:
    """
    Fetch a single page of data from the API.

    Args:
        offset: Number of records to skip
        limit: Maximum number of records to return (default: 200)

    Returns:
        Parsed JSON response as a dictionary
    """
    # TODO
    pass

def fetch_all_measurements() -> list:
    """
    Fetch all measurements by handling pagination.

    Returns:
        List of all measurement records
    """
    all_measurements = []
    offset = 0
    limit = LIMIT

    while True:
        try:
            print(f"Fetching records with offset {offset}, limit {limit}...")
            response = fetch_page(offset, limit)
            data = response.get('data', [])

            if not data:
                break

            all_measurements.extend(data)

            # If we got fewer records than the limit, we've reached the last page
            if len(data) < limit:
                break

            offset += limit

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            break

    return all_measurements


def compute_pollutant_means(measurements: list) -> dict:
    """
    Compute mean values for each pollutant type.

    Args:
        measurements: List of measurement records

    Returns:
        Dictionary mapping pollutant type to mean value
    """


    # TODO
    pass


def write_csv(pollutant_means: dict, filename: str = "pollutant_means.csv"):
    """
    Write pollutant means to a CSV file.

    Args:
        pollutant_means: Dictionary mapping pollutant type to mean value
        filename: Output CSV filename
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        # TODO
        pass

def main():
    """Main function to execute the analysis."""
    print("Fetching air quality measurements...")

    # Fetch all measurements with pagination
    measurements = fetch_all_measurements()
    total_count = len(measurements)

    print(f"Total count of measurements found: {total_count}")

    if total_count == 0:
        print("No measurements found. Exiting.")
        return

    # Compute means for each pollutant
    print("Computing mean values for each pollutant...")
    pollutant_means = compute_pollutant_means(measurements)

    if not pollutant_means:
        print("No valid pollutant data found. Exiting.")
        return

    # Write to CSV
    csv_filename = "pollutant_means.csv"
    write_csv(pollutant_means, csv_filename)

    print(f"Results written to {csv_filename}")
    print(f"Found {len(pollutant_means)} different pollutants:")
    for pollutant, mean_value in sorted(pollutant_means.items()):
        print(f"  {pollutant}: {mean_value:.4f}")


if __name__ == "__main__":
    main()
