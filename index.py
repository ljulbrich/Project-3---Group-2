# Import the dependencies
from flask import Flask, jsonify, render_template

# Import local dependencies
from webscraper import webscraper

if __name__ == "__main__":
    #################################################
    # Database Setup
    #################################################

    #################################################
    # Flask Setup
    #################################################

    app = Flask(__name__)


    #################################################
    # Flask Routes
    #################################################
    @app.route('/')
    def home():
        return render_template('home.html')



    @app.route('/long-term-price/<ticker>')
    def long_term_price(ticker):

        # Add ticker list to MongoDB
        # call webscraper
        scraped_data = webscraper(ticker)

        # Pass JSON data to template
        return render_template('long-term-price.html', scraped_data=scraped_data)
        
    app.run(debug=True)