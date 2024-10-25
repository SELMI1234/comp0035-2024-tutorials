from pathlib import Path

from tutorialpkg.mypkg2.mymodule2_1 import calculate_area_of_circle
from tutorialpkg.mypkg2.mymodule2_2 import fetch_user_data

if __name__ == '__main__':
    # The functions are in the modules in mypkg2. You will need to import them.
    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")

    mock_database = {
    1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    42: {'name': 'Bob', 'email': 'bob@example.com', 'age': 45},
    }

    # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))

    # Locate the data file `paralmpics_raw.csv` relative to this file
    csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')
    csv_file_v2 = Path(__file__).parent.parent / 'data' / 'paralympics_events_raw.csv'

    # Check if the file exists
    if csv_file.exists():
        print(f"CSV file found: {csv_file}")
    else:
        print("CSV file not found.")

    # Check if the alternative path (csv_file_v2) also exists, just to demonstrate both methods
    if csv_file_v2.exists():
        print(f"CSV file found (using csv_file_v2): {csv_file_v2}")
    else:
        print("CSV file not found (using csv_file_v2).")
