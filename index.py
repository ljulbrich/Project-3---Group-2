# Import the dependencies
from flask import Flask, jsonify, render_template
from pathlib import Path
import regex as re
import pandas as pd

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

        if __name__ == '__main__':
            app.run(debug=True)

    @app.route('/long-term-price/<ticker>')
    def long_term_price(ticker):

        # Add ticker list to MongoDB
        if ticker in ASX_list['ASX code']:
            # call webscraper
            scraped_data = webscraper(ticker)

            # Convert DataFrame to JSON string
            json_data = df.to_json(orient='records')

            # Pass JSON data to template
            return render_template('index.html', json_data=json_data)
            
