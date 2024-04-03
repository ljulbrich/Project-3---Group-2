import yfinance
import pandas as pd
import json

def live_view(ticker_input):
    start_date = '1990-01-01'
    ticker_name = yfinance.Ticker(ticker_input)
    history_start_end = ticker_name.history(start=start_date, end=None)

    


    with open('resources/livedata.json', 'w') as outfile:
        json.dump()
