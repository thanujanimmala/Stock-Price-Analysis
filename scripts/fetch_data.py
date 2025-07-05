# scripts/fetch_data.py

import yfinance as yf
import os
import pandas as pd

def fetch_stock_data(tickers, start_date, end_date, save_path="data/raw"):
    os.makedirs(save_path, exist_ok=True)

    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
        if not df.empty:
            file_path = os.path.join(save_path, f"{ticker.replace('.NS', '')}.csv")
            df.to_csv(file_path)
            print(f"Saved: {file_path}")
        else:
            print(f"⚠️ No data found for {ticker}")

if __name__ == "__main__":
    # Define your stocks and time range here
    tickers = ["TCS.NS", "RELIANCE.NS", "INFY.NS"]
    start_date = "2000-01-01"
    end_date = "2025-07-03"

    fetch_stock_data(tickers, start_date, end_date)
