from pymongo import MongoClient
import yfinance as yf
import numpy as np
import pandas as pd

#the companies database in mongo  was imported from nasdaq_companies.csv from the resources folder
#nasdaq_companies.csv is downloaded from NASDAQ offcial website, and imported by bash command below:
#mongoimport --type csv -d stocks -c nasdaq --headerline --drop nasdaq_companies.csv

def rand_com_data():
    #connect to the mongo db
    mongo = MongoClient(port=27017)
    stock_db = mongo['stocks']
    nasdaq = stock_db["nasdaq"]

    #it has over 7k records, and I only want companies that at least have been trading for over a year
    query = {'IPO Year': {"$lt":2022}}
    field = {'Symbol':1}
    total = nasdaq.count_documents(query)

    #this will randomly choose a company who meets the query
    random_index = np.random.randint(total-1)
    results = nasdaq.find(query, field)
    rand_com = results[random_index]['Symbol']

    #send the lucky one to yahoo finance API
    rand_ticker = yf.Ticker(rand_com)
    #by requesting the past 12 months share price data, it will return a dataframe thats groupby date, so I need to reset its index
    df = rand_ticker.history(period="12mo").reset_index()
    #this original date format is annoying
    datetime_series = pd.to_datetime(df.Date)
    # Extract the date part (without time)
    date_series = datetime_series.dt.strftime('%Y-%m-%d').to_list()

    #this method was originally designed for another purpose
    #-------------------------------------------------------
    #now, I need to randomly choose one of the four prices (open, high, low, close) as that day's final share price
    #because when we check on share prices, we only check it for a short period of time and come bace later to check again
    #this is to simulate that, because at a given moment the share price can be at either one the four
    #all_data = [df.Open.to_list(),df.High.to_list(),df.Low.to_list(), df.Close.to_list()]
    #rand_idx = np.random.randint(len(all_data)-1)
    #data=[]
    #randomly choose a list and access to that list's index and collect it and round it
    #for i in range (len(date_series)):
    #    data.append(round(all_data[rand_idx][i],2))
    #------------------------------------------------------

    high = df.High.to_list()
    low = df.Low.to_list()
    return rand_com, date_series, high, low

def save_data(db_name, collection_name, com_name, data):
    mongo = MongoClient(port=27017)
    # Get the database object (creates it if it doesn't exist)
    db = mongo[db_name]
    #same as above
    collection = db[collection_name]

    collection.insert_one(
    {
        'stock': com_name,
        'full_name': data['name'],
        'bid_price': data['bid'],
        'bid_amount': data['amount'],
        'email': data['email'],
        'mobile': data['mobile']
    })
