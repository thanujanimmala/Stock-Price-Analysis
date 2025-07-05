import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from prophet import Prophet
from prophet.plot import plot_plotly
import os
from scripts.generate_pdf import generate_pdf
import plotly.io as pio

st.set_page_config(page_title="Stock Price Analyzer", layout="wide")

st.title("Stock Price Analysis (2000–2025 + Forecast)")

# Sidebar: Choose data source
st.sidebar.markdown("### Choose Data Source")
uploaded_file = st.sidebar.file_uploader(
    "Upload Your Own Stock CSV", type=["csv"])

# Initialize
df = None
ticker = None

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, parse_dates=["Date"])
        df.set_index("Date", inplace=True)
        ticker = "Uploaded CSV"
        st.sidebar.success("Custom CSV loaded successfully.")
    except Exception as e:
        st.sidebar.error(f"Failed to load file: {e}")
else:
    ticker = st.sidebar.selectbox("Choose Stock", ["TCS", "RELIANCE", "INFY"])
    file_path = f"data/processed/{ticker}.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, parse_dates=["Date"])
        df.set_index("Date", inplace=True)
    else:
        st.error(f"File not found: {file_path}")

if df is not None:
    # Optional: Calculate MA_252 if not present
    if "MA_252" not in df.columns:
        df["MA_252"] = df["Close"].rolling(window=252).mean()

    # Sidebar: Date range selector
    min_date = df.index.min().date()
    max_date = df.index.max().date()
    start = st.sidebar.date_input(
        "Start Date", min_date, min_value=min_date, max_value=max_date)
    end = st.sidebar.date_input(
        "End Date", max_date, min_value=min_date, max_value=max_date)
    filtered_df = df.loc[str(start):str(end)]

    # Show table checkbox
    if st.sidebar.checkbox("Show Cleaned Data"):
        st.subheader("Cleaned Stock Data")
        st.dataframe(filtered_df)

    # Line chart
    st.subheader(f"{ticker} Closing Price & 1-Year Moving Average")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    filtered_df["Close"].plot(ax=ax1, label="Close")
    filtered_df["MA_252"].plot(ax=ax1, label="1-Year MA", color="orange")
    ax1.set_ylabel("Price (₹)")
    ax1.legend()
    st.pyplot(fig1)
    fig1.savefig("closing_price.png")

    # Annual Return Bar Chart
    st.subheader(f"{ticker} Annual Returns (% Change)")
    annual_df = filtered_df["Close"].resample(
        "Y").last().pct_change().dropna() * 100
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    annual_df.plot(kind='bar', ax=ax2, color='skyblue')
    ax2.set_ylabel("Annual Return (%)")
    ax2.set_xlabel("Year")
    ax2.set_title("Annual Returns")
    st.pyplot(fig2)
    fig2.savefig("annual_return.png")

    # Prophet Forecast
    st.subheader("Forecast Stock Prices (Next 2 Years)")
    prophet_df = filtered_df.reset_index()[["Date", "Close"]].rename(
        columns={"Date": "ds", "Close": "y"})
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=730)
    forecast = model.predict(future)

    fig3 = model.plot(forecast)
    plt.title(f"{ticker} Forecast (Next 2 Years)")
    plt.tight_layout()
    plt.savefig("forecast.png")
    st.pyplot(fig3)

    if st.checkbox("Show raw forecast data"):
        st.write(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())

    # Export to PDF
    st.subheader("Export Report as PDF")

    if st.button("Download PDF Report"):
        with st.spinner("Generating report..."):
            pdf_path = generate_pdf(
                ticker,
                start,
                end,
                [
                    ("Closing Price & 1-Year MA", "closing_price.png"),
                    ("Annual Returns", "annual_return.png"),
                    ("Forecast", "forecast.png"),
                ]
            )
            with open(pdf_path, "rb") as f:
                st.download_button("Download Report", f,
                                   file_name="stock_report.pdf")
