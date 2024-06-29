import yfinance as yf
import pandas as pd
from tabulate import tabulate

# Define the stock symbols and your holdings
symbols = ['NVDA', 'AAPL', 'TSLA']  # Example symbols
holdings = {
    'NVDA': 10,  # Example holdings
    'AAPL': 15,
    'TSLA': 5
}
purchase_prices = {
    'NVDA': 120.0,  # Correct purchase prices
    'AAPL': 195.0,
    'TSLA': 170.0
}

# Fetch the stock data
data = []
for symbol in symbols:
    stock = yf.Ticker(symbol)
    info = stock.info
    current_price = info.get('regularMarketPrice', 'N/A')
    low = info.get('dayLow', 'N/A')
    high = info.get('dayHigh', 'N/A')
    forward_pe = info.get('forwardPE', 'N/A')
    holding = holdings[symbol]
    purchase_price = purchase_prices[symbol]
    change = (current_price - purchase_price) * holding if current_price != 'N/A' else 'N/A'
    data.append([symbol, current_price, low, high, forward_pe, holding, change])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Symbol', 'Price', 'Low', 'High', 'Forward P/E', 'Holding', 'Change'])

# Print the table
print(tabulate(df, headers='keys', tablefmt='pretty'))
