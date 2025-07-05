# main.py

from scripts.fetch_data import fetch_stock_data
from scripts.clean_data import clean_stock_data
from scripts.analyze_trends import analyze_trends
from scripts.visualize import plot_stock_price_and_ma, plot_annual_returns

def run_pipeline():
    tickers = ["TCS.NS", "RELIANCE.NS", "INFY.NS"]
    tickers_clean = ["TCS", "RELIANCE", "INFY"]

    print("📥 Fetching stock data...")
    fetch_stock_data(tickers, "2000-01-01", "2025-07-03")

    print("\n🧹 Cleaning data...")
    clean_stock_data()

    print("\n📈 Analyzing trends...")
    analyze_trends()

    print("\n📊 Generating visualizations...")
    for ticker in tickers_clean:
        plot_stock_price_and_ma(ticker)
        plot_annual_returns(ticker)

    print("\n✅ All steps completed!")

if __name__ == "__main__":
    run_pipeline()
