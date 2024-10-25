from pathlib import Path
import pandas as pd

# Define the function to describe the DataFrame
def describe_data(df):
    """
    Prints a summary of the DataFrame.

    Parameters:
    df (DataFrame): A pandas DataFrame containing the data to be described.

    Returns:
    None
    """
    print("Summary of the DataFrame:")
    print(df.info())
    print("\nBasic Statistics:")
    print(df.describe())
    print("\nFirst 5 Rows:")
    print(df.head())

# Main code to read the CSV and use the function
if __name__ == '__main__':
    # Locate the data file using pathlib
    csv_file = Path(__file__).parent.parent.parent.joinpath('data', 'paralympics_raw.csv')

    # Check if the CSV file exists before reading it
    if csv_file.exists():
        print(f"CSV file found at: {csv_file}")
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Describe the data using the describe_data function
        describe_data(df)
    else:
        print("CSV file not found.")
