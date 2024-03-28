# Import the dependencies.
from flask import Flask, jsonify, render_template
from pathlib import Path
import regex as re
import pandas as pd

# Importing selenium components
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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
    query_start = 'https://au.finance.yahoo.com/quote/';
    query_end = '?.tsrc=fin-srch'
    csv_path = Path('Resources/ASX_Listed_Companies_25-03-2024_02-42-20_AEDT.csv')
    ASX_list = pd.read_csv(csv_path)
    article_dict = {}
    
    if ticker in ASX_list['ASX code']:
        query_URL = f"{query_start}{ticker}{query_end}"

        # Setting up the selenium webdriver
        options = Options()
        options.add_argument('--headless=new')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get(query_URL)
        articles = driver.find_elements(By.CSS_SELECTOR, 'li[class="js-stream-content Pos(r)"]')


        for article in articles:
            raw_html = article.get_attribute('outerHTML')

            # Creating regex patterns
            title_pattern = r'(?:</u>)(.*?)(?:</a>)'
            blurb_pattern = r'(?:\(0\)">)(.*?)(?:</p>)'
            link_pattern = r'(?:href=")(.*?)(?: data-uuid)'

            # Performing a regex search
            title = re.search(title_pattern, raw_html)
            blurb = re.search(blurb_pattern, raw_html)
            link = re.search(link_pattern, raw_html)
            article_dict[title.group(1)] = {blurb.group(1):link.group(1)}

        # Closing the webdriver
        driver.quit()
        
        # run article blurbs through sentiment analysis algorithm
        # run blurbs through algorithm which selects the most common words

        
    else:
        print('Invalid stock ticker!')
        # insert logic to go to an invalid stock ticker page


# find x and y values