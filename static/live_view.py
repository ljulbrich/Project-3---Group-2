import yfinance
import pandas as pd
import json

def live_view(ticker_input, start_date, end_date):
    ticker_name = yfinance.Ticker(ticker_input)
    time_period = ['d', 'mo', 'y']
    shares = ticker_name.get_shares_full(start="2022-01-01", end=None)
    history_start_end = ticker_name.history(start='2024-03-21', end='2024-03-28')
    history_period = ticker_name.history(period='1mo')
