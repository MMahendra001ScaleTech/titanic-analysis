import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.title("📈 Interactive Stock Market Dashboard")

# Sidebar
st.sidebar.header("Dashboard Settings")

# Stock symbol input
symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, GOOGL)", "AAPL")

# Date range selection
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(start_date, end_date),
    max_value=end_date
)

try:
    # Fetch stock data
    stock = yf.Ticker(symbol)
    df = stock.history(start=date_range[0], end=date_range[1])

    # Company info
    info = stock.info
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"{info.get('longName', symbol)}")
        st.write(f"Sector: {info.get('sector', 'N/A')}")
        st.write(f"Industry: {info.get('industry', 'N/A')}")
    
    with col2:
        st.metric(
            "Current Price",
            f"${df['Close'].iloc[-1]:.2f}",
            f"{((df['Close'].iloc[-1] - df['Close'].iloc[-2])/df['Close'].iloc[-2]*100):.2f}%"
        )

    # Candlestick chart
    st.subheader("Stock Price Chart")
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)

    # Trading volume
    st.subheader("Trading Volume")
    volume_fig = go.Figure(data=[go.Bar(x=df.index, y=df['Volume'])])
    volume_fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Volume",
        height=300
    )
    st.plotly_chart(volume_fig, use_container_width=True)

    # Key statistics
    st.subheader("Key Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Market Cap", f"${info.get('marketCap', 0)/1e9:.2f}B")
    with col2:
        st.metric("P/E Ratio", f"{info.get('trailingPE', 'N/A')}")
    with col3:
        st.metric("52 Week High", f"${info.get('fiftyTwoWeekHigh', 0):.2f}")
    with col4:
        st.metric("52 Week Low", f"${info.get('fiftyTwoWeekLow', 0):.2f}")

except Exception as e:
    st.error(f"Error fetching data for {symbol}. Please check the stock symbol and try again.")
    st.error(f"Error details: {str(e)}")