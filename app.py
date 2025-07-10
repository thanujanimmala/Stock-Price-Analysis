import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import os
import yfinance as yf
from scripts.generate_pdf import generate_pdf_bytes

st.set_page_config(page_title="Stock Price Analyzer", layout="wide")
st.title("📊 Stock Price Analysis (2000–2025 + Forecast)")

# Sidebar: Select data source
st.sidebar.markdown("### Data Source")

data_mode = st.sidebar.radio(
    "Select Source:", ["Predefined Stocks", "Enter Ticker", "Upload CSV"])

df = None
ticker = None

# 📁 Option 1: Upload CSV
if data_mode == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader(
        "Upload Your Own Stock CSV", type=["csv"])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file, parse_dates=["Date"])
            df.set_index("Date", inplace=True)
            ticker = "Uploaded CSV"
            st.sidebar.success("Custom CSV loaded successfully.")
        except Exception as e:
            st.sidebar.error(f"Failed to load file: {e}")

# ✅ Option 2: Predefined stocks
elif data_mode == "Predefined Stocks":
    ticker = st.sidebar.selectbox("Choose Stock", ["TCS", "RELIANCE", "INFY"])
    file_path = f"data/processed/{ticker}.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, parse_dates=["Date"])
        df.set_index("Date", inplace=True)
    else:
        st.error(f"File not found: {file_path}")

# 🌐 Option 3: Yahoo Finance fetch
elif data_mode == "Enter Ticker":
    user_ticker = st.sidebar.text_input(
        "Enter stock ticker (e.g., TCS.NS, AAPL, INFY.NS):")
    if user_ticker:
        try:
            data = yf.download(
                user_ticker, start="2000-01-01", end="2025-12-31")
            if data.empty:
                st.sidebar.error(
                    "No data found. Please check the ticker symbol.")
            else:
                df = data.copy()
                # Flatten multi-index columns if any (some tickers return multi-index columns)
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = ['_'.join(filter(None, map(str, col))).strip() for col in df.columns.values]
                # Ensure Date index
                df["Date"] = df.index
                df.set_index("Date", inplace=True)
                ticker = user_ticker.upper()
                st.sidebar.success(f"Fetched data for {ticker}")
        except Exception as e:
            st.sidebar.error(f"Error fetching data: {e}")
    else:
        st.sidebar.info("Please enter a stock ticker.")

# Proceed only if df is loaded
if df is not None and not df.empty:
    # Find the Close column dynamically
    close_cols = [col for col in df.columns if col.lower().startswith("close")]
    if not close_cols:
        st.error("Close price column not found in the data.")
    else:
        close_col = close_cols[0]  # use the first Close column found

        # Calculate 1-year MA if missing
        ma_col = "MA_252"
        if ma_col not in df.columns:
            df[ma_col] = df[close_col].rolling(window=252).mean()

        # Sidebar: Date range
        min_date = df.index.min().date()
        max_date = df.index.max().date()
        start = st.sidebar.date_input(
            "Start Date", min_date, min_value=min_date, max_value=max_date)
        end = st.sidebar.date_input(
            "End Date", max_date, min_value=min_date, max_value=max_date)

        filtered_df = df.loc[str(start):str(end)]

        # Show data
        if st.sidebar.checkbox("Show Cleaned Data"):
            st.subheader("📋 Cleaned Stock Data")
            st.dataframe(filtered_df)

        # 📈 Line Chart
        st.subheader(f"{ticker} Closing Price & 1-Year Moving Average")
        fig1, ax1 = plt.subplots(figsize=(10, 4))
        filtered_df[close_col].plot(ax=ax1, label="Close")
        if ma_col in filtered_df.columns:
            filtered_df[ma_col].plot(ax=ax1, label="1-Year MA", color="orange")
        ax1.set_ylabel("Price (₹)")
        ax1.legend()
        st.pyplot(fig1)
        fig1.savefig("closing_price.png")

        # 📊 Annual Return Bar Chart
        st.subheader(f"{ticker} Annual Returns (% Change)")
        annual_df = filtered_df[close_col].resample("Y").last().pct_change().dropna() * 100
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        annual_df.plot(kind='bar', ax=ax2, color='skyblue')
        ax2.set_ylabel("Annual Return (%)")
        ax2.set_xlabel("Year")
        ax2.set_title("Annual Returns")
        st.pyplot(fig2)
        fig2.savefig("annual_return.png")

        # ... continue with forecasting logic (also use close_col)


    # 🔮 Prophet Forecast
    st.subheader("Forecast Stock Prices (Next 2 Years)")

    # Prepare prophet_df for forecasting
    df_reset = filtered_df.reset_index()

    # Find the correct Close column (handles multi-index flattening)
    close_cols = [col for col in df_reset.columns if col.lower().startswith("close")]
    if close_cols:
        close_col = close_cols[0]

        prophet_df = pd.DataFrame({
            "ds": df_reset["Date"],
            "y": pd.to_numeric(df_reset[close_col], errors="coerce")
        }).dropna()

        if prophet_df.empty:
            st.warning("⚠️ Not enough valid data to generate forecast.")
        else:
            try:
                model = Prophet()
                model.fit(prophet_df)
                future = model.make_future_dataframe(periods=730)
                forecast = model.predict(future)

                fig3 = model.plot(forecast)
                plt.title(f"{ticker} Forecast (Next 2 Years)")
                plt.tight_layout()
                plt.savefig("forecast.png")
                st.pyplot(fig3)

                if st.checkbox("Show raw forecast data", key="forecast_raw_data"):
                    st.write(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())
            except Exception as e:
                st.error(f"Forecasting failed: {e}")
    else:
        st.error("Close price column not found for forecasting.")

else:
    st.info("Please select a stock or upload a file to begin analysis.")

# 📄 Export to PDF
# Only show export option if filtered data is available
if df is not None and not filtered_df.empty:
    st.subheader("Export Report as PDF")

    if st.button("Download PDF Report"):
        with st.spinner("Generating report..."):
            pdf_bytes = generate_pdf_bytes(
                ticker,
                start,
                end,
                [
                    ("Closing Price & 1-Year MA", "closing_price.png"),
                    ("Annual Returns", "annual_return.png"),
                    ("Forecast", "forecast.png"),
                ]
            )
        st.download_button(
            label="Download Report",
            data=pdf_bytes,
            file_name="stock_report.pdf",
            mime="application/pdf"
        )
