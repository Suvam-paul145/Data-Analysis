import yfinance as yf
import pandas as pd
import streamlit as st

st.write(
         "# Welcome to the Stock Price App")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-1-1')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)  