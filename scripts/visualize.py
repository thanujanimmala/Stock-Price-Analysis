# scripts/visualize.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

def plot_stock_price_and_ma(ticker, data_path="data/processed", output_path="reports/figures"):
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(data_path, f"{ticker}.csv")

    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close Price")
    plt.plot(df.index, df["MA_252"], label="1-Year Moving Average", color="orange")
    plt.title(f"{ticker} Closing Price & Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price (INR)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, f"{ticker}_trend.png"))
    plt.close()


def plot_annual_returns(ticker, data_path="data/processed", output_path="reports/figures"):
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(data_path, f"annual_return_{ticker}.csv")

    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")

    plt.figure(figsize=(10, 4))
    df.plot(kind="bar", legend=False, color="skyblue")
    plt.title(f"{ticker} Annual Return (%)")
    plt.ylabel("Return %")
    plt.xlabel("Year")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, f"{ticker}_returns.png"))
    plt.close()

if __name__ == "__main__":
    tickers = ["TCS", "RELIANCE", "INFY"]

    for ticker in tickers:
        print(f"Generating plots for {ticker}...")
        plot_stock_price_and_ma(ticker)
        plot_annual_returns(ticker)
    print("✅ All visualizations saved in reports/figures/")
