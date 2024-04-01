# Import the dependencies.
from flask import Flask, render_template
from xiang import er_plot, company_details, company_name, get_news
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

    #try-catch is for early debugging purpose, not really useful tho. keep it as a future example
    try:
        er_image = er_plot(stock)
        c_data = company_details(stock)
        c_name = company_name(stock)
        news = get_news(stock)
    except Exception as e:
        error_message = str(e)
        return render_template("main.html", error_message=error_message)
    
    return render_template('main.html', er_image = er_image, c_data = c_data, c_name=c_name, news=news)

#################################################
# Run the app
#################################################
if __name__ == '__main__':
    app.run(debug=True)