import yfinance as yf
import pandas as pd
import streamlit as st
import datetime

st.title("📈 Stock Price App")

# User input
tickerSymbol = st.text_input("Enter stock ticker (e.g., GOOGL, AAPL)", "GOOGL")
start_date = st.date_input("Start date", datetime.date(2010, 1, 1))
end_date = st.date_input("End date")

# Get data
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start=start_date, end=end_date)

# Show charts
st.subheader(f"{tickerSymbol} Closing Price")
st.line_chart(tickerDf.Close)

st.subheader(f"{tickerSymbol} Volume")
st.line_chart(tickerDf.Volume)

# Optional: Show raw data
if st.checkbox("Show raw data"):
    st.write(tickerDf.tail())