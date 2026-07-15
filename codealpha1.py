print("Stock Portfolio Tracker")
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 145
}

print("Available Stocks:")

for stock, price in stock_prices.items():
    print(stock, "-", price)
    