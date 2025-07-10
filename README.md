# 📊 Stock Price Analysis (2000–2025 + Forecast)

---

A full-featured web application built with **Streamlit**, **Prophet**, and **yfinance** to:

- Analyze historical stock price trends  
- Forecast future prices using time series models  
- Export charts and insights into a neat **PDF report**

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
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # All required Python libraries
├── README.md               # You're reading it!
│
├── data/
│   ├── raw/                # (Optional) Raw stock data files
│   └── processed/          # Preprocessed stock CSVs
│
├── reports/
│   └── figures/            # Saved plots used in PDF
│
├── scripts/
│   ├── fetch_data.py       # Fetch stock data (optional utility)
│   ├── clean_data.py       # Data cleaning logic
│   ├── analyze_trends.py   # MA, annual return calculations
│   ├── visualize.py        # Reusable plot functions
│   └── generate_pdf.py     # Create PDF report using FPDF
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
