# scripts/analyze_trends.py

import pandas as pd
import os

def analyze_trends(input_path="data/processed", output_path="data/processed"):
    for file in os.listdir(input_path):
        if file.endswith(".csv"):
            file_path = os.path.join(input_path, file)
            df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

            print(f"Analyzing trends for {file}...")

            # Add 1-year (252 trading days) Moving Average
            df['MA_252'] = df['Close'].rolling(window=252).mean()

            # Compute annual returns (Year-end price % change)
            yearly = df['Adj Close'].resample('Y').last()
            annual_return = yearly.pct_change().dropna() * 100

            # Save moving average to CSV
            df.to_csv(os.path.join(output_path, file))

            # Save annual returns separately
            annual_return_df = annual_return.to_frame(name='Annual Return (%)')
            annual_return_file = os.path.join(output_path, f"annual_return_{file}")
            annual_return_df.to_csv(annual_return_file)

            print(f"Saved annual returns: {annual_return_file}")

if __name__ == "__main__":
    analyze_trends()
