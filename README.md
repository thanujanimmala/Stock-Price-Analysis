# 📈 Stock Price Analysis Web App

A web application to analyze historical stock data, visualize trends, forecast future prices, and generate PDF reports — built using **Streamlit**, **Pandas**, and **Plotly**.

---

## 🚀 Features

-  Fetch stock data (TCS, Reliance, Infosys) from 2000–2025 using **Yahoo Finance**
-  Interactive line and bar charts
-  252-day Moving Average calculation
-  Forecast future stock prices using Prophet
-  Upload custom CSV files
-  Download cleaned data in Excel format
-  Generate PDF analysis report with graphs

---

## 🌐 Live Demo

Try it here:  
🔗 [https://stock-price-analysis-7x6q.onrender.com](https://stock-price-analysis-7x6q.onrender.com)

---

## 🧪 Technologies Used

- **Python 3.10+**
- **Streamlit**
- **Pandas**
- **Plotly**
- **Prophet**
- **yfinance**
- **fpdf**
- **Kaleido** (for image export)

---

## 📁 Project Structure

stock-price-analysis/
├── app.py # Main Streamlit web app
├── main.py # CLI pipeline runner 
├── README.md # Project overview
├── requirements.txt # Project dependencies
├── report.pdf # Sample generated report
├── annual_return.png # Saved chart image
├── closing_price.png # Saved chart image
├── forecast.png # Saved chart image

├── data/ # Folder for raw and cleaned data
│ ├── raw/
│ └── processed/

├── scripts/ # Python scripts used in pipeline
│ ├── fetch_data.py
│ ├── clean_data.py
│ ├── analyze_trends.py
│ ├── generate_pdf.py
│ └── utils.py

├── notebooks/ 
└── reports/
└── figures/ # Output figures for reporting

