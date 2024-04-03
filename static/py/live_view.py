import yfinance
import pandas as pd
import json

def live_view(ticker_input):
    start_date = '2014-01-01'
    ticker_name = yfinance.Ticker(ticker_input)
    history_start_end = ticker_name.history(start=start_date, end=None)

    live_data_df = pd.DataFrame(history_start_end)
    live_data_df.reset_index(inplace=True)
    live_data_json = live_data_df.to_json(orient='index')

    return live_data_json
