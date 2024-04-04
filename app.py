# Import the dependencies.
from flask import Flask, render_template, request, jsonify
from xiang import er_plot, company_details, company_name, get_news, main_plot
from database import rand_com_data, save_data
from static.py.live_view import live_view
from static.py.webscraper import webscraper
import yfinance as yf

#################################################
# Flask Setup
#################################################
app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return render_template('index.html')

#this application needs a lot validation check, to avoid bad input to inprove user experience, but this is a demo for plotting
#the purpose of the project is to display data visualizaitons, so the user experience will be ignored here
@app.route("/<ticker>", methods=["GET", "POST"])
def main(ticker):
    stock = yf.Ticker(ticker)
    
    er_image = er_plot(stock)
    company_data = company_details(stock)
    com_name = company_name(stock)
    news = get_news(stock)
    ticker_date, ticker_high, ticker_low = main_plot(stock)

    return render_template('main.html', er_image = er_image, company_data = company_data, com_name=com_name, 
                           news=news, ticker_date=ticker_date, ticker_high=ticker_high, ticker_low=ticker_low)

@app.route("/simulation", methods=["GET", "POST"])
def simulation():
    stock_symbol, stock_date, stock_high, stock_low = rand_com_data()

    if request.method == 'POST':
        form_data = request.form
        save_data('trade','requests', stock_symbol, form_data)

        return render_template('thank.html')
    
    return render_template('simulation.html', stock_symbol=stock_symbol, stock_date=stock_date, stock_high=stock_high, stock_low=stock_low)

@app.route('/long-term-price/<ticker>')
def long_term_price(ticker):
    scraped_data = webscraper(ticker)
    live_data = live_view(ticker)

    # Pass JSON data to template
    return render_template('long-term-price.html', scraped_data=scraped_data, live_data=live_data)

@app.route("/roytop20")
def roy():
    return render_template('Top_20_ASX_Stocks.html')


#################################################
# Run the app
#################################################
if __name__ == '__main__':
    app.run(debug=True)