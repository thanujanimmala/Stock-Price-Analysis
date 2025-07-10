# 📊 Stock Price Analysis (2000–2025 + Forecast)
---

A full-featured web app built with **Streamlit**, **Prophet**, and **yfinance** to analyze stock price trends, forecast future prices, and export results to a clean **PDF report**.

🌐 **Live App:** [Click to Open](https://stock-price-analysis-7x6q.onrender.com/)

---

## 📌 Features
---

- ✅ **Preloaded Stocks**: Analyze TCS, RELIANCE, INFY directly.
- 🔍 **Enter Custom Ticker**: Fetch any stock using Yahoo Finance.
- 📂 **Upload Your Own CSV**: Bring your own historical stock data.
- 📈 **Visual Charts**:
  - Closing Price with 1-Year Moving Average
  - Annual Returns (%)
  - Forecasting with Facebook Prophet (Next 2 Years)
- 📅 **Flexible Date Range Filtering**
- 🧾 **Download PDF Report** with all visualizations
- 🧼 Optionally display raw cleaned or forecast data

---

## 🗂️ Project Structure
---
```bash
Stock-Price-Analysis/
├── app.py                  # Streamlit App
├── requirements.txt        # Dependencies
├── README.md               # Documentation
│
├── data/
│   ├── raw/                # Raw downloaded CSVs
│   └── processed/          # Cleaned stock data
│
├── reports/
│   └── figures/            # Saved graphs for PDF
│
├── scripts/
│   ├── fetch_data.py       # Fetch from Yahoo Finance
│   ├── clean_data.py       # Data cleaning
│   ├── analyze_trends.py   # MA & annual return logic
│   ├── generate_pdf.py     # Generate report using FPDF
│   └── visualize.py        # Save and show graphs
```
## 📦 Installation & Setup Guide

Follow these steps to run the project locally on your system:

###  1. Clone the Repository

First, clone this GitHub repository to your local machine.

```bash
git clone https://github.com/thanujanimmala/Stock-Price-Analysis.git
cd Stock-Price-Analysis
```

### 2. Install All Dependencies
Install the required Python libraries using the requirements.txt file:

```bash

pip install -r requirements.txt
```

### 3. Run the Streamlit App
Once everything is installed, launch the Streamlit app:

```bash

streamlit run app.py
```
This will open the web application in your default browser at:

```arduino

http://localhost:8501
```
### 📄 Example CSV Format
```csv

Date,Close
2020-01-01,400.5
2020-01-02,405.2
...
```


## 📦 Built With
---

• Streamlit – UI framework

• yfinance – Stock data source

• Prophet – Time-series forecasting

• [Pandas, Matplotlib, Seaborn] – Data processing & visualization

• FPDF – PDF generation


## 🧠 Future Ideas
---

• Compare multiple tickers side-by-side

• Add technical indicators (RSI, MACD)

• Add volume-based analysis

• Add historical performance summary panel

## 📜 License
---
This project is licensed under the MIT License.
