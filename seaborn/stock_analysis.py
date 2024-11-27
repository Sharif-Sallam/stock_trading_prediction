# Import required libraries
import warnings
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Suppress specific FutureWarning from yfinance
warnings.filterwarnings("ignore", category=FutureWarning, module="yfinance")

# Step 1: Fetch real stock data
# Replace 'AAPL' with the ticker symbol of your choice
ticker = "AAPL"  # Apple Inc.
stock_data = yf.download(ticker, start="2024-09-01", end="2024-11-26")

# Add moving averages
stock_data["7Day_MA"] = stock_data["Close"].rolling(window=7).mean()
stock_data["14Day_MA"] = stock_data["Close"].rolling(window=14).mean()

# Reset index for easier plotting
stock_data.reset_index(inplace=True)

# Step 2: Visualize stock prices with Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(stock_data["Date"], stock_data["Close"], label="Close Price", color="blue")
plt.title(f"{ticker} Stock Prices (Matplotlib)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.legend()
plt.show()

# Step 3: Enhance the plot with Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x="Date", y="Close", data=stock_data, label="Close Price", color="blue")
sns.lineplot(x="Date", y="7Day_MA", data=stock_data, label="7-Day MA", color="orange")
sns.lineplot(x="Date", y="14Day_MA", data=stock_data, label="14-Day MA", color="green")
plt.title(f"{ticker} Stock Prices with Moving Averages (Seaborn)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Step 4: Create an interactive candlestick chart with Plotly
fig = go.Figure(data=[go.Candlestick(
    x=stock_data["Date"],
    open=stock_data["Open"],
    high=stock_data["High"],
    low=stock_data["Low"],
    close=stock_data["Close"],
    increasing_line_color='green',
    decreasing_line_color='red'
)])
fig.update_layout(
    title=f"Interactive Candlestick Chart for {ticker}",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    xaxis_rangeslider_visible=True
)
fig.show()
