import yfinance as yf

# Create a ticker object for the stock you want to retrieve data for
ticker = yf.Ticker("AAPL")
# msft_ticker = yf.Ticker("msft")

# Get historical price data
historical_data = ticker.history(period="1mo")

# Print the historical data
print(historical_data)

