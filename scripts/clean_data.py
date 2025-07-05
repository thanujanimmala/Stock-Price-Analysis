import pandas as pd
import os

def clean_stock_data(input_path="data/raw", output_path="data/processed"):
    os.makedirs(output_path, exist_ok=True)

    for file in os.listdir(input_path):
        if file.endswith(".csv"):
            file_path = os.path.join(input_path, file)

            df = pd.read_csv(file_path, header=0)

            print(f"Cleaning {file}...")

            # Rename 'Price' column to 'Date' because it contains dates
            if 'Price' in df.columns:
                df.rename(columns={'Price': 'Date'}, inplace=True)

            # Convert 'Date' column to datetime
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

            # Drop rows with invalid dates
            df = df.dropna(subset=['Date'])

            # Drop any other missing values
            df.dropna(inplace=True)

            # Set 'Date' as index
            df.set_index('Date', inplace=True)

            # Save cleaned data without the index column in CSV (optional)
            output_file = os.path.join(output_path, file)
            df.to_csv(output_file)
            print(f"Saved cleaned data: {output_file}")

if __name__ == "__main__":
    clean_stock_data()
