# scripts/utils.py

import os
import pandas as pd

def load_data(ticker, cleaned=False):
    base_folder = "data/processed" if cleaned else "data/raw"
    file_path = os.path.join(base_folder, f"{ticker}.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, parse_dates=["Date"])
        df.set_index("Date", inplace=True)
        return df
    return None

def load_forecast_data(ticker):
    forecast_path = f"data/forecast/forecast_{ticker}.csv"
    if os.path.exists(forecast_path):
        df = pd.read_csv(forecast_path, parse_dates=["ds"])
        return df
    return None

def load_annual_returns(ticker):
    annual_path = f"data/processed/annual_return_{ticker}.csv"
    if os.path.exists(annual_path):
        df = pd.read_csv(annual_path, parse_dates=["Date"])
        df.set_index("Date", inplace=True)
        return df
    return None
