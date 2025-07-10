# 📊 Stock Price Analysis (2000–2025 + Forecast)

---

A full-featured web application built with **Streamlit**, **Prophet**, and **yfinance** to:

- Analyze historical stock price trends  
- Forecast future prices using time series models  
- Export charts and insights into a neat **PDF report**
---

## 🚀 Project Overview

• This web app is designed to help users analyze stock price data comprehensively and intuitively. With **preloaded popular Indian stocks** (TCS, Reliance, Infosys), the ability to **fetch any stock data live from Yahoo Finance**, or **upload your own stock price history CSV**, this tool covers diverse use cases. 

• The app provides interactive charts such as moving averages and annual returns alongside Facebook Prophet’s forecasting model to offer both historical visual insights and future price predictions, helping users make smarter decisions.


🌐 **Live Demo** → [Click Here to Open](https://stock-price-analysis-7x6q.onrender.com/)

---

## ✅ Features

---

- 📦 **Predefined Stocks**: Analyze **TCS**, **RELIANCE**, and **INFY**
- 🔍 **Custom Ticker Input**: Search and fetch live stock data using Yahoo Finance
- 📁 **Upload CSV**: Analyze your own stock data file
- 📅 **Date Range Filter**: Focus on specific time periods
- 📈 **Visual Charts**:
  - Line Chart: Closing Price + 1-Year Moving Average
  - Bar Chart: Annual Return (% change)
  - Prophet Forecast: Next 2 years (with confidence interval)
- 📄 **Download PDF Report** with all visualizations
- 📋 Toggle to view raw cleaned data or forecast output

---

## 🗂️ Project Structure

---

```
Stock-Price-Analysis/
├── app.py                   # Main Streamlit application
├── main.py                  # Main helper functions (outside scripts)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── data/
│   ├── raw/                 # Raw downloaded stock CSV files
│   └── processed/           # Cleaned/processed stock CSV files
├── reports/
│   └── figures/             # Generated plots/images for PDF reports
├── scripts/
│   ├── fetch_data.py        # Functions to fetch stock data from Yahoo Finance
│   ├── clean_data.py        # Data cleaning functions
│   ├── analyze_trends.py    # Functions to calculate moving averages, returns
│   ├── generate_pdf.py      # PDF report generation functions
│   ├── visualize.py         # Plotting and visualization functions
│   └── utils.py             # Utility/helper functions
└── .gitignore               # Files/folders to ignore in Git

```

---

## 🛠️ Installation & Setup Guide

---

> 💡 Make sure Python 3.8+ is installed before starting

### 1. 🔁 Clone the Repository

```bash
git clone https://github.com/thanujanimmala/Stock-Price-Analysis.git
cd Stock-Price-Analysis
```

### 2. 🧪 (Optional) Create a Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. 📦 Install All Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. 🚀 Run the Streamlit App

```bash
streamlit run app.py
```

> This opens in your browser at:  
> `http://localhost:8501`

---

## 📄 Example CSV Format (For Upload Option)

```csv
Date,Close
2020-01-01,410.50
2020-01-02,415.60
...
```

---

## 🧰 Built With

---

- **[Streamlit](https://streamlit.io/)** – App framework
- **[Prophet](https://facebook.github.io/prophet/)** – Forecasting
- **[yfinance](https://pypi.org/project/yfinance/)** – Stock data fetching
- **[Pandas](https://pandas.pydata.org/)** – Data wrangling
- **[Matplotlib & Seaborn](https://seaborn.pydata.org/)** – Visualizations
- **[FPDF](https://pyfpdf.readthedocs.io/)** – PDF generation

---

## 🚀 Future Improvements

---

- 📊 Compare multiple stocks side-by-side  
- 📉 Add technical indicators like RSI, MACD  
- 📈 Volume and volatility analysis  
- 📌 Summary metrics dashboard (CAGR, max drawdown, etc.)

---

## 📜 License

---

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute with attribution.

---

## 🔗 Links

---

- 🔍 GitHub Repo: [thanujanimmala/Stock-Price-Analysis](https://github.com/thanujanimmala/Stock-Price-Analysis)
- 🌐 Live Demo: [Render Hosted App](https://stock-price-analysis-7x6q.onrender.com/)

---
