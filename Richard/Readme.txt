import yfinance as yf
#show the result of current price
import requests
from bs4 import BeautifulSoup
def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    stock_hist = stock.history(period='1d')
    return stock_hist['Close'][0]

stocks=['CROX','DECK','ONON','WWW','DBI','WEYS','SHOO','SKX','BIRK','RCKY','VRA','NKE']

for symbol in stocks:
    try:
        stock_price = get_stock_price(symbol)
        print(f"The current price of {symbol} is {stock_price}")
    except Exception as e:
        print(f"couldn't find stock {symbol}: {e}")




#Data exported to 52WeekChange_data_1.csv

import yfinance as yf
import csv

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    stock_hist = stock.history(period='1d')
    return stock_hist['Close'][0]

stocks = ['CROX', 'DECK', 'ONON', 'WWW', 'DBI', 'WEYS', 'SHOO', 'SKX', 'BIRK', 'RCKY', 'VRA', 'NKE']

data = []

for symbol in stocks:
    try:
        stock_price = get_stock_price(symbol)
        # Round stock price to two decimal places
        stock_price = round(stock_price, 2)
        data.append([symbol, stock_price])
    except Exception as e:
        print(f"Couldn't find stock {symbol}: {e}")

# Exporting data to CSV file
csv_file = "stock_prices.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Current Price"])  # Write header
    writer.writerows(data)

print(f"Data exported to {csv_file}")

#Data exported to 52WeekChange_data_1.csv
import yfinance as yf
import csv

def get_52week_change(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    return info.get('52WeekChange', 'N/A')

stocks = ['CROX', 'DECK', 'ONON', 'WWW', 'DBI', 'WEYS', 'SHOO', 'SKX', 'BIRK', 'RCKY', 'VRA', 'NKE']

data = []

for symbol in stocks:
    try:
        week_change = get_52week_change(symbol)
        week_change  = round(week_change , 2)
        data.append([symbol, week_change])
    except Exception as e:
        print(f"Couldn't find stock {symbol}: {e}")

# Exporting data to CSV file
csv_file = "52WeekChange_data_1.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "52WeekChange"])  # Write header
    writer.writerows(data)

print(f"Data exported to {csv_file}")

#Data exported to stock_data_1.csv
import yfinance as yf
import csv

def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    return info

stocks = ['CROX', 'DECK', 'ONON', 'WWW', 'DBI', 'WEYS', 'SHOO', 'SKX', 'BIRK', 'RCKY', 'VRA', 'NKE']

data = []

for symbol in stocks:
    try:
        stock_info = get_stock_info(symbol)
        name = stock_info.get('shortName', 'N/A')
        pe_ratio = stock_info.get('trailingPE', 'N/A')
        # Round PE ratio to two decimal places
        pe_ratio = round(pe_ratio, 2) if pe_ratio != 'N/A' else 'N/A'
        data.append([name, pe_ratio])
    except Exception as e:
        print(f"Couldn't find stock {symbol}: {e}")

# Exporting data to CSV file
csv_file = "stock_data_1.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "PE Ratio"])  # Write header
    writer.writerows(data)

print(f"Data exported to {csv_file}")

#Plot of current stock price
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('stock_prices.csv')

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Current Price'], color='skyblue')
plt.xlabel('Stock Symbol')
plt.ylabel('Current Price')
plt.title('Current Prices of Stocks')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot to local computer
plt.savefig('stock_prices_bar_plot.png')

# Show plot (optional)
plt.show()

#Plot of 52 weeks change
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('52WeekChange_data_1.csv')

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['52WeekChange'], color='red')
plt.xlabel('Stock Symbol')
plt.ylabel('52WeekChange')
plt.title('52WeekChange of Stocks')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot to local computer
plt.savefig('52WeekChange_bar_plot.png')

# Show plot (optional)
plt.show()


#Plot of PE ratio
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('stock_data_1.csv')

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['PE Ratio'], color='green')
plt.xlabel('Stock Name')
plt.ylabel('PE Ratio')
plt.title('PE Ratio of Stocks')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot to local computer
plt.savefig('stock_data_1_bar_plot.png')

# Show plot (optional)
plt.show()


