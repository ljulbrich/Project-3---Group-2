import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import pandas as pd

def er_plot(stock):
    #get the dates which are the columns
    dates = stock.income_stmt.columns.to_list()

    #its better to do regex than hard code these labels, if have more time
    date_labels = ['2020', '2021', '2022', '2023']

    revenues = []
    earnings = []
    for date in reversed(dates):
        #unit in billion
        revenues.append(round((stock.income_stmt[date]['Total Revenue']/1000000000),2))
        earnings.append(round((stock.income_stmt[date]['Net Income']/1000000000),2))
    data = {'Revenues': revenues, 'Earnings': earnings}

    x = np.arange(len(dates))
    #width of bars
    width = 0.25
    multiplier = 0

    #example of group data plotting
    fig, ax = plt.subplots(layout='constrained', figsize=(6, 6))

    for attribute, measurement in data.items():
        offset = width * multiplier
        rects = ax.bar(x+offset, measurement, width=width, label=attribute)
        ax.bar_label(rects, padding=5)
        multiplier += 1

    ax.set_ylabel('Billion Dollars')
    ax.set_title(stock.info['shortName'] + " Yearly Earnings vs Revenues")
    ax.set_xticks(x+width/2, date_labels)
    ax.legend(loc='upper left', ncols=2)
    #set ylim only when the min value is > 0, otherwise the graph would look weird
    if (min(min(earnings), min(revenues)) > 0 ):
        ax.set_ylim(0, max(max(earnings), max(revenues))*1.15)

    #transfer img data to html
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format="png")
    img_data = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
    
    return img_data

def company_details(stock):
    return [
    {'Previous close': stock.info['previousClose']},
    {'Open': stock.info['open']},
    {'Day range': f"{stock.info['dayLow']} - {stock.info['dayHigh']}"},
    {'52-week range': f"{stock.info['fiftyTwoWeekLow']} - {stock.info['fiftyTwoWeekHigh']}"},
    {'Volumn': stock.info['volume']},
    {'Avg. volumn': stock.info['averageVolume']},
    {'Market cap': f"{round((stock.info['marketCap']/1000000000),3)}B"},
    {'Beta (5Y monthly)': stock.info['beta']},
    {'PE raio(TTM)': round(stock.info['trailingPE'],2)},
    {'Revenue/share': round(stock.info['revenuePerShare'],2)},
    {'Profit Margins': round(stock.info['profitMargins'],2)},
    {'EPS(TTM)': stock.info['trailingEps']}
    ]

def company_name(stock):
    return stock.info['longName']

def get_news(stock):
    data = []
    no_image = 'https://as2.ftcdn.net/v2/jpg/04/70/29/97/1000_F_470299797_UD0eoVMMSUbHCcNJCdv2t8B2g1GVqYgs.jpg'
    for news in stock.news:
        if ('thumbnail' in news.keys()):
            data.append([{'url': news['thumbnail']['resolutions'][0]['url']},
                        {'title': news['title']},
                        {'link': news['link']}
                        ])
        else:
            data.append([{'url': no_image},
                        {'title': news['title']},
                        {'link': news['link']}
                        ])
    return data

#same function from database.py
def main_plot(stock):
    df = stock.history(period="12mo").reset_index()
    datetime_series = pd.to_datetime(df.Date)
    date_series = datetime_series.dt.strftime('%Y-%m-%d').to_list()
    high = df.High.to_list()
    low = df.Low.to_list()
    return date_series, high, low

    